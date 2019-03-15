# -*- coding: utf-8 -*-
# =============================================================================
#Developers : 
#       Shashank Sharma(shashankrnr32@gmail.com)
#           - Primary UI Rendering
#           - Kannada to English Translate
#           - JSON Based Database Implementation
#           - Media Player
#           - Audio Integration
#       
#       Varun S S(varunsridhar614@gmail.com)
#           - Synthesize Backend
#           - FestAPI.sh
#
#Description : 
#       Main Application Executable
#      
#Modules Used :
#       Uses AppResources.py and Application.py to Render UI
#       Uses FestAPI.sh to run Speech Synthesis Project
#       Uses GTranslate.py Module for English-Kannada Translation
# =============================================================================

import sys,time,os,shutil
from PyQt4 import QtCore, QtGui

class PlayThread(QtCore.QThread):
    #==========================================================================
    #Thread Implementation for Play Progress Bar
    #==========================================================================
    
    def __init__(self,seconds,parent = None):
        #======================================================================
        #Constructor : Calls the Parent Constructor
        #======================================================================
        super(PlayThread,self).__init__(parent)
        self.seconds = seconds/100
    
    def set_seconds(self,seconds):
        #======================================================================
        #Setter Function for `seconds`
        #Each percentage of the progress bar occurs for `seconds` sec
        #======================================================================
        self.seconds = seconds/100
        
    def run(self):
        #======================================================================
        #Description :
        #   Overrides run() from QtCore.QThread
        #   Called when the thread is started
        #======================================================================
        
        signal = 0
        
        while signal != 100:
            #Thread sleeps for `seconds` sec
            self.msleep(self.seconds*1000)
            
            #Increment in Percentage
            signal += 1
            
            #Emit SIGNAL : bar_percent that is caught by Implementation Window
            self.emit(QtCore.SIGNAL('bar_percent'),signal)
        self.emit(QtCore.SIGNAL('bar_percent'),0)


from Application import Ui_MainWindow
import GTranslate
from Database import Database as db
from PyQt4.phonon import Phonon

class MyApp(QtGui.QMainWindow):

    def __init__(self, *args, **kwargs):
        QtGui.QWidget.__init__(self, parent = None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #Configure Buttons
        self.button_config()
        
        #Configure Shortcuts
        self.shortcut_config()
        
        #Configure Status Bar
        self.statusBar = QtGui.QStatusBar()
        self.setStatusBar(self.statusBar)
        
        #Disable Maximize Button
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        
        #Connect to Database (JSON)
        self.database = db('res/db.json')

        #Defines a Audio Output Device
        self.audio_output = Phonon.AudioOutput(Phonon.MusicCategory,self)
        
        #Define an Audio Object
        self.audio = Phonon.MediaObject(self)
        self.audio.stateChanged.connect(self.start_progress_bar)
        self.audio.totalTimeChanged.connect(self.update_thread_time)
        
        #Create a Runnable Thread
        self.play_thread = PlayThread(seconds = 0)
        
        #Connect Signal to Update Progress Bar
        self.connect(self.play_thread,QtCore.SIGNAL('bar_percent'), self.update_progress_bar)
        
        #`audio` is the source and `audio_output` is the sink : CREATE PATH
        Phonon.createPath(self.audio,self.audio_output)
        
        #Create an About Window Instance
        self.about_page = AboutDialog(parent = self)
        
    
    def shortcut_config(self):
        #======================================================================
        #Description:
        #   Configure all Keyboard Shortcuts of the UI
        #======================================================================
        
        #Delete Key clears All Text
        self.shortcut = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Delete),self)
        self.shortcut.activated.connect(self.reset_all)
    
    
    def button_config(self):
        #======================================================================
        #Description:
        #   Configure all Buttons of the UI
        #======================================================================
        
        #Synthesize Button Action
        self.ui.syn_button.pressed.connect(self.synthesize)
        self.ui.syn_button.setEnabled(False)
        
        #Translate Button Action
        self.ui.translate_button.clicked.connect(self.translate)
        self.ui.translate_button.setEnabled(False)
        
        #Play Button Action
        self.ui.play_button.clicked.connect(self.play)
        
        #Stop Button Action
        self.ui.stop_button.clicked.connect(self.stop)
        
        #Reset Button Action
        self.ui.reset_button_1.clicked.connect(lambda : self.ui.kan_input.setPlainText(''))
        self.ui.reset_button_1.setEnabled(False)
        self.ui.reset_button_2.clicked.connect(lambda: self.ui.en_input.setPlainText(''))
        self.ui.reset_button_2.setEnabled(False)
        
        #Signal Configurations
        self.connect(self.ui.kan_input, QtCore.SIGNAL('textChanged()'), self.kan_input_onChange)
        self.connect(self.ui.en_input, QtCore.SIGNAL('textChanged()'), self.en_input_onChange)
    
    
    def show_status(self,msg,t = 1000):
        #======================================================================
        #Description:
        #   Implementation of Status Bar
        #
        #Param:
        #   msg:str - Message
        #   t:int - Time for message to be active (ms)
        #======================================================================
        self.statusBar.showMessage(msg,t)
        self.ui_update()
    
    @classmethod
    def ui_update(self):
        #======================================================================
        #Description:
        #   UI Updates simultaneously as the backend process runs
        #======================================================================
        QtGui.qApp.processEvents()

    
    def synthesize(self):
        #======================================================================
        #Description:
        #   Handler Function for Synthesize Button
        #
        #Algorithm:
        #   - Start
        #   - Disable Button
        #   - Acquire Text and Write into $PRODIR/etc/temp.txt
        #   - Call Shell API (FestAPI.sh)
        #   - Write the Text into res/db.txt
        #   - End
        #======================================================================
        
        start_time = time.time()                                                                                
        
        #Disable Synthesize Button
        self.ui.syn_button.setEnabled(False)
        self.ui_update()
        
        #Acquire Text
        kan_txt = self.ui.kan_input.toPlainText()
        
        #Always-Unique Wave Number
        wavenum = str(time.strftime("%Y%m%d_%H%M%S"))
        
        #Write Kannada Text to temp.txt
        with open(os.environ['PRODIR']+'/etc/temp.txt', 'w') as temp_file:
            temp_file.write('( kan_{} \" {} \")'.format(wavenum,kan_txt))
        
        self.show_status('Processing...', 0)                                                                    
        
        #DSP option Checked/Unchecked
        if self.ui.dsp.isChecked():
            os.system('./FestAPI.sh 1 {}'.format(wavenum))
        else:
            os.system('./FestAPI.sh 0 {}'.format(wavenum))
        
        #All Done...
        self.show_status('Done... ({}s)'.format('%.3f'%(time.time()-start_time)),2500)                          
        
        #Store all Synthesized Files in res/db.txt
        self.database.add_entry(kan_txt,wavenum,update = True)
        
        #ReEnable Buttons Again
        self.ui.syn_button.setEnabled(True)
        self.ui_update()


    def translate(self):
        #======================================================================
        #Description:
        #   Handler Function for Translate Button
        #======================================================================
        
        #Disable Translate Button
        self.ui.translate_button.setEnabled(False)
        self.ui_update()
        
        #Acquire Text
        en_text = self.ui.en_input.toPlainText()
        
        self.show_status('Translating...')
        
        #Call GTranslate Module
        kn_text = GTranslate.en2kn(en_text) 
        self.ui.kan_input.setPlainText(kn_text)
        
        self.show_status('Done...')
        
        #Re-Enable Translate Button
        self.ui.translate_button.setEnabled(True)
        self.ui_update()
    
    def reset_1(self):
        #======================================================================
        #Description:
        #   Handler Function for Reset_1 Button
        #======================================================================
        pass

    def reset_2(self):
        #======================================================================
        #Description:
        #   Handler Function for Reset_2 Button
        #======================================================================
        pass
        
    def reset_all(self):
        #======================================================================
        #Description:
        #   Handler Function for Delete Key shortcut
        #======================================================================
        self.ui.kan_input.setPlainText('')
        self.ui.en_input.setPlainText('')
    
    def kan_input_onChange(self):
        #======================================================================
        #Description:
        #   This function Runs everytime Kannada Text Changes
        #======================================================================
        
        kan_txt = self.ui.kan_input.toPlainText()
        if kan_txt == '':
            self.ui.syn_button.setEnabled(False)
            self.ui.reset_button_1.setEnabled(False)
        else:
            self.ui.syn_button.setEnabled(True)
            self.ui.reset_button_1.setEnabled(True)
    
    def en_input_onChange(self):
        #======================================================================
        #Description:
        #   This function Runs everytime English Text Changes
        #======================================================================
        en_txt = self.ui.en_input.toPlainText()
        if en_txt == '':
            self.ui.translate_button.setEnabled(False)
            self.ui.reset_button_2.setEnabled(False)
        else:
            self.ui.translate_button.setEnabled(True)
            self.ui.reset_button_2.setEnabled(True)
    
    def play(self):
        #======================================================================
        #Description:
        #   Handler Function for Play Button
        #======================================================================
        
        #Implementation of Reading Correct Wav Files to Play Yet to Develop...
        
        #Set Audio File to Play [C]
        self.audio.setCurrentSource(Phonon.MediaSource('/home/shashank/Music/kan_0001.wav'))
        
        #Play the Audio
        self.audio.play()
    
    def stop(self):
        #======================================================================
        #Description:
        #   Handler Function for Stop Button
        #======================================================================
        
        #Stop the Audio
        self.audio.stop()
        
        if self.play_thread.isRunning():
            self.play_thread.terminate()
        self.ui.play_progress.setValue(0)
    
    def update_thread_time(self,milliseconds):
        #======================================================================
        #Update Thread Time every time new file loads
        #======================================================================
        
        #80 ms lost in other execution (DEPENDS ON CPU)
        error = 80
        
        #Update thread time
        self.play_thread.set_seconds(self.audio.totalTime()/(1000+error))
    
    
    def start_progress_bar(self,new_state,old_state):
        #======================================================================
        #Start Progress Bar only after wav file loads
        #======================================================================
        if new_state == 2:
            #Start Progress Bar Thread
            self.play_thread.start()
    
    def update_progress_bar(self,percent):
        #======================================================================
        #Description:
        #   Threaded Progress Bar update
        #   Reentrant function runs when play_thread emits SIGNAL : bar_percent
        #======================================================================
        self.ui.play_progress.setValue(percent)

def setEnv():
    #======================================================================
    #Description:
    #   Set Environment Variables of EST, Festvoc, SPTK, Project and App
    #   Change Paths as needed
    #======================================================================
    os.environ['ESTDIR'] = '/home/shashank/Project/Main/speech_tools'
    os.environ['FESTVOXDIR'] = '/home/shashank/Project/Main/festvox'
    os.environ['SPTKDIR'] = '/home/shashank/Project/Main/sptk'
    os.environ['PRODIR'] = '/home/shashank/Project/Main/cmu_indic_kan_female'
    os.environ['WAVDIR'] = 'home/shashank/Project/WavFiles'
    os.environ['APP'] = os.getcwd()


#Main Function        
if __name__ == "__main__":
    
    #Set Permissions and Env Variables
    setEnv()
    os.system('chmod 755 FestAPI.sh')
    
    #Create and Start Application
    app = QtGui.QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    
    #Remove __pycache__ Folder once execution is complete
    shutil.rmtree('./__pycache__',ignore_errors=True)
    sys.exit(app.exec_())