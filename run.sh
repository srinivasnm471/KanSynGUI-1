#!/bin/sh
###############################################################
#Developer : Shashank Sharma
#
#Description : Executable File for GUI Application
#
#License : MIT
###############################################################

cd App/
echo Installing Required Packages

# Soundstretch for Pitch Shift
if [ $(dpkg-query -W -f='${Status}' soundstretch 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  sudo apt-get install nano;
fi


#pip3 for installing Python Packages
if [ $(dpkg-query -W -f='${Status}' python3-pip 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
   sudo apt-get install -y python3-pip
fi

#Google Translate Package
python3 -c "import google.cloud.translate"
if [ $? -eq 1 ];
then
   pip3 install google-cloud-translate
fi

#python-qt4 For User Interface
if [ $(dpkg-query -W -f='${Status}' python-qt4 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
   sudo apt-get install -y python-qt4 pyqt4-dev-tools python-qt4 qt4-designer
fi

echo Building User Interface
pyuic4 Application.ui -o Application.py

echo Building Resources
pyrcc4 AppResources.qrc  -o AppResources_rc.py -py3

echo Starting Application..
python3 Main.py

echo Exiting Application
rm AppResources_rc.py
rm Application.py
cd ..
