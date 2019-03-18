#!/bin/sh

# =============================================================================
# Copyright (C) 2019  Shashank Sharma, Varun S S
# 
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>
# =============================================================================

# =============================================================================
#Developer : Shashank Sharma
#Description : Executable File for GUI Application
# =============================================================================
clear
echo ==========================================
echo Kannada Speech Synthesis
echo ==========================================
echo "Copyright (C) 2019  Shashank Sharma
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome 
to redistribute it under certain conditions."
echo ==========================================
echo

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
   sudo apt-get install -y python-qt4 pyqt4-dev-tools python-qt4 qt4-designer python3-pyqt4.phonon
fi

echo Building User Interface
pyuic4 Application.ui -o Application.py

echo Building Resources
pyrcc4 AppResources.qrc  -o AppResources_rc.py -py3

echo Starting Application...
python3 Main.py

echo Exiting Application...
rm AppResources_rc.py
rm Application.py
cd ..
