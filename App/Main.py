# -*- coding: utf-8 -*-

# =============================================================================
# Developer : Shashank Sharma
# Description : 
#     Main Application Executable
#     Uses AppResources.py and Application.py to Render UI
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
        
        self.button_config()
        
            
    def button_config(self):  
        #Synthesize Button Action
        self.ui.syn_button.clicked.connect(self.synthesize)
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
    
    
    #Handler Function for Synthesize Button    
    def synthesize(self):
        self.ui.syn_button
        
        kan_txt = self.ui.kan_input.toPlainText()
        wavenum = str(time.strftime("%Y%m%d_%H%M%S"))
        
        #Write Kannada Text to temp.txt
        with open('res/temp.txt', 'w') as temp_file:
            temp_file.write('( kan_{} \" {} \")'.format(wavenum,kan_txt))
        
        print(wavenum)
        os.system('cp res/temp.txt $PRODIR/etc/temp.txt')
        
        #DSP option Checked/Unchecked
        if self.ui.dsp.isChecked():
            os.system('./FestAPI.sh 1 {}'.format(wavenum))
        else:
            os.system('./FestAPI.sh 0 {}'.format(wavenum))
        
        #Store all Synthesized Files in res/db.txt
        with open('res/db.txt', 'a') as file:
            file.write('\n( kan_{} \" {} \"){}'.format(wavenum,kan_txt,int(self.ui.dsp.isChecked())))
        
    #Handler Function for Translate Button
    def translate(self):
        en_text = self.ui.en_input.toPlainText()
        kn_text = GTranslate.en2kn(en_text) 
        self.ui.kan_input.setPlainText(kn_text)
        
    #Handler Function for Reset Button
    def reset(self):
        self.ui.en_input.setPlainText('')
        self.ui.kan_input.setPlainText('')
    
    #This function Runs everytime Kannada Text Changes
    def kan_input_onChange(self):
        kan_txt = self.ui.kan_input.toPlainText()
        if kan_txt == '':
            self.ui.syn_button.setEnabled(False)
            self.ui.reset_button_1.setEnabled(False)
        else:
            self.ui.syn_button.setEnabled(True)
            self.ui.reset_button_1.setEnabled(True)
    
    def en_input_onChange(self):
        en_txt = self.ui.en_input.toPlainText()
        if en_txt == '':
            self.ui.translate_button.setEnabled(False)
            self.ui.reset_button_2.setEnabled(False)
        else:
            self.ui.translate_button.setEnabled(True)
            self.ui.reset_button_2.setEnabled(True)

def setEnv():
    os.environ['ESTDIR'] = '/home/shashank/Project/Main/speech_tools'
    os.environ['FESTVOXDIR'] = '/home/shashank/Project/Main/festvox'
    os.environ['SPTKDIR'] = '/home/shashank/Project/Main/sptk'
    os.environ['PRODIR'] = '/home/shashank/Project/Main/cmu_indic_kan_female'
    os.environ['APP'] = os.getcwd()
#Main Method        
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
    
    
    