# -*- coding: utf-8 -*-
# =============================================================================
# Developer : 
#       Shashank Sharma
#       Varun S S
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
from Application import Ui_MainWindow
import GTranslate

class MyApp(QtGui.QMainWindow):

    def __init__(self, *args, **kwargs):
        QtGui.QWidget.__init__(self, parent = None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #Configure Buttons
        self.button_config()
        
        #Configure Status Bar
        self.statusBar = QtGui.QStatusBar()
        self.setStatusBar(self.statusBar)
            
    def button_config(self):  
        #======================================================================
        #Description:
        #   Configure all Buttons of the UI
        #=====================================================================
        
        #Synthesize Button Action
        self.ui.syn_button.pressed.connect(self.synthesize)
        self.ui.syn_button.setEnabled(False)
        
        #Translate Button Action
        self.ui.translate_button.clicked.connect(self.translate)
        self.ui.translate_button.setEnabled(False)
        
        #Reset Button Action
        self.ui.reset_button_1.clicked.connect(self.reset)
        self.ui.reset_button_1.setEnabled(False)
        self.ui.reset_button_2.clicked.connect(self.reset)
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
        with open('res/db.txt', 'a') as file:
            file.write('\n( kan_{} \" {} \"){}'.format(wavenum,kan_txt,int(self.ui.dsp.isChecked())))
        
        #ReEnable Buttons Again
        self.ui.syn_button.setEnabled(True)
        self.ui_update()

    
    def translate(self):
        #======================================================================
        #Description:
        #   Handler Function for Translate Button
        #======================================================================
        
        en_text = self.ui.en_input.toPlainText()
        kn_text = GTranslate.en2kn(en_text) 
        self.ui.kan_input.setPlainText(kn_text)
        
    
    def reset(self):
        #======================================================================
        #Description:
        #   Handler Function for Reset Button
        #======================================================================
        
        self.ui.en_input.setPlainText('')
        self.ui.kan_input.setPlainText('')
    
    
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
  
    
    