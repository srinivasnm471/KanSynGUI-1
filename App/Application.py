# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Application.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(920, 538)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 538))
        MainWindow.setMaximumSize(QtCore.QSize(928, 538))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.rit_logo = QtGui.QLabel(self.centralwidget)
        self.rit_logo.setGeometry(QtCore.QRect(-1, -20, 921, 111))
        self.rit_logo.setObjectName(_fromUtf8("rit_logo"))
        self.project_title = QtGui.QLabel(self.centralwidget)
        self.project_title.setGeometry(QtCore.QRect(2, 110, 921, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Manjari"))
        self.project_title.setFont(font)
        self.project_title.setObjectName(_fromUtf8("project_title"))
        self.dsp = QtGui.QCheckBox(self.centralwidget)
        self.dsp.setGeometry(QtCore.QRect(20, 270, 189, 22))
        self.dsp.setChecked(True)
        self.dsp.setObjectName(_fromUtf8("dsp"))
        self.reset_button_2 = QtGui.QPushButton(self.centralwidget)
        self.reset_button_2.setEnabled(True)
        self.reset_button_2.setGeometry(QtCore.QRect(270, 430, 81, 41))
        self.reset_button_2.setWhatsThis(_fromUtf8(""))
        self.reset_button_2.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/clear_button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_button_2.setIcon(icon)
        self.reset_button_2.setIconSize(QtCore.QSize(25, 25))
        self.reset_button_2.setDefault(False)
        self.reset_button_2.setFlat(False)
        self.reset_button_2.setObjectName(_fromUtf8("reset_button_2"))
        self.listView_2 = QtGui.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(470, 160, 441, 321))
        font = QtGui.QFont()
        font.setKerning(True)
        self.listView_2.setFont(font)
        self.listView_2.setMouseTracking(False)
        self.listView_2.setFrameShape(QtGui.QFrame.Box)
        self.listView_2.setFrameShadow(QtGui.QFrame.Plain)
        self.listView_2.setLineWidth(1)
        self.listView_2.setMidLineWidth(0)
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.syn_button = QtGui.QPushButton(self.centralwidget)
        self.syn_button.setGeometry(QtCore.QRect(360, 270, 81, 41))
        self.syn_button.setWhatsThis(_fromUtf8(""))
        self.syn_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/syn_button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.syn_button.setIcon(icon1)
        self.syn_button.setIconSize(QtCore.QSize(35, 35))
        self.syn_button.setDefault(True)
        self.syn_button.setObjectName(_fromUtf8("syn_button"))
        self.kan_input = QtGui.QTextEdit(self.centralwidget)
        self.kan_input.setGeometry(QtCore.QRect(20, 190, 421, 71))
        self.kan_input.setFrameShape(QtGui.QFrame.StyledPanel)
        self.kan_input.setFrameShadow(QtGui.QFrame.Raised)
        self.kan_input.setObjectName(_fromUtf8("kan_input"))
        self.columnView_2 = QtGui.QColumnView(self.centralwidget)
        self.columnView_2.setGeometry(QtCore.QRect(10, 160, 441, 321))
        self.columnView_2.setFrameShape(QtGui.QFrame.Box)
        self.columnView_2.setFrameShadow(QtGui.QFrame.Plain)
        self.columnView_2.setObjectName(_fromUtf8("columnView_2"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 170, 93, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 140, 901, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(451, 160, 20, 321))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.en_input = QtGui.QTextEdit(self.centralwidget)
        self.en_input.setGeometry(QtCore.QRect(20, 350, 421, 71))
        self.en_input.setFrameShadow(QtGui.QFrame.Raised)
        self.en_input.setObjectName(_fromUtf8("en_input"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 330, 93, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.translate_button = QtGui.QPushButton(self.centralwidget)
        self.translate_button.setGeometry(QtCore.QRect(360, 430, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.translate_button.setFont(font)
        self.translate_button.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/translate_button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.translate_button.setIcon(icon2)
        self.translate_button.setIconSize(QtCore.QSize(25, 25))
        self.translate_button.setObjectName(_fromUtf8("translate_button"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 410, 107, 9))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setItalic(False)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.reset_button_1 = QtGui.QPushButton(self.centralwidget)
        self.reset_button_1.setEnabled(True)
        self.reset_button_1.setGeometry(QtCore.QRect(270, 270, 81, 41))
        self.reset_button_1.setWhatsThis(_fromUtf8(""))
        self.reset_button_1.setText(_fromUtf8(""))
        self.reset_button_1.setIcon(icon)
        self.reset_button_1.setIconSize(QtCore.QSize(25, 25))
        self.reset_button_1.setDefault(False)
        self.reset_button_1.setFlat(False)
        self.reset_button_1.setObjectName(_fromUtf8("reset_button_1"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(478, 390, 425, 80))
        self.frame.setFocusPolicy(QtCore.Qt.NoFocus)
        self.frame.setFrameShape(QtGui.QFrame.WinPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.progressBar = QtGui.QProgressBar(self.frame)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(7, 60, 411, 10))
        self.progressBar.setProperty("value", 22)
        self.progressBar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.pushButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 10, 40, 40))
        self.pushButton_2.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.columnView_2.raise_()
        self.listView_2.raise_()
        self.rit_logo.raise_()
        self.project_title.raise_()
        self.dsp.raise_()
        self.reset_button_2.raise_()
        self.syn_button.raise_()
        self.kan_input.raise_()
        self.label_7.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.en_input.raise_()
        self.label_8.raise_()
        self.translate_button.raise_()
        self.label.raise_()
        self.reset_button_1.raise_()
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuLicense = QtGui.QMenu(self.menubar)
        self.menuLicense.setObjectName(_fromUtf8("menuLicense"))
        self.menuSource_Code = QtGui.QMenu(self.menubar)
        self.menuSource_Code.setObjectName(_fromUtf8("menuSource_Code"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionDevelopers = QtGui.QAction(MainWindow)
        self.actionDevelopers.setObjectName(_fromUtf8("actionDevelopers"))
        self.actionMentor = QtGui.QAction(MainWindow)
        self.actionMentor.setObjectName(_fromUtf8("actionMentor"))
        self.actionAbout_Project = QtGui.QAction(MainWindow)
        self.actionAbout_Project.setObjectName(_fromUtf8("actionAbout_Project"))
        self.actionPython_Source = QtGui.QAction(MainWindow)
        self.actionPython_Source.setObjectName(_fromUtf8("actionPython_Source"))
        self.actionUI_Source = QtGui.QAction(MainWindow)
        self.actionUI_Source.setObjectName(_fromUtf8("actionUI_Source"))
        self.menuAbout.addAction(self.actionDevelopers)
        self.menuAbout.addAction(self.actionMentor)
        self.menuAbout.addAction(self.actionAbout_Project)
        self.menuSource_Code.addAction(self.actionPython_Source)
        self.menuSource_Code.addAction(self.actionUI_Source)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuLicense.menuAction())
        self.menubar.addAction(self.menuSource_Code.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Kannada Speech Synthesis", None))
        self.rit_logo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/img/img/rit_logo.png\" width=\"250\" height=\"125\"/></p></body></html>", None))
        self.project_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#55557f;\">Kannada Speech Synthesis</span></p></body></html>", None))
        self.dsp.setText(_translate("MainWindow", "Apply Signal Processing", None))
        self.reset_button_2.setToolTip(_translate("MainWindow", "Clear", None))
        self.syn_button.setToolTip(_translate("MainWindow", "Synthesize", None))
        self.label_7.setText(_translate("MainWindow", "Kannada Text", None))
        self.label_8.setText(_translate("MainWindow", "English Text", None))
        self.translate_button.setToolTip(_translate("MainWindow", "Translate (en-kn)", None))
        self.label.setText(_translate("MainWindow", "Powered by Google Translate", None))
        self.reset_button_1.setToolTip(_translate("MainWindow", "Clear", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.menuLicense.setTitle(_translate("MainWindow", "License", None))
        self.menuSource_Code.setTitle(_translate("MainWindow", "Source Code", None))
        self.actionDevelopers.setText(_translate("MainWindow", "Developers", None))
        self.actionMentor.setText(_translate("MainWindow", "Mentor", None))
        self.actionAbout_Project.setText(_translate("MainWindow", "About Project", None))
        self.actionPython_Source.setText(_translate("MainWindow", "Python Source", None))
        self.actionUI_Source.setText(_translate("MainWindow", "UI Source", None))

import AppResources
