#!/bin/sh
cd App
echo Building User Interface
pyuic4 Application.ui -o Application.py

echo Building Resources
pyrcc4 AppResources.qrc  -o AppResources_rc.py -py3

echo Starting Application..
python3 Main.py

echo Exiting Application
rm AppResources_rc.py
rm Application.ui
cd ..
