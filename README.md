# GUI Documentation
All commands given in this documentation is to be executed from `/App ` Directory

##  Libraries Installation
The following Libraries are to be installed before running the Application

#### Linux/Ubuntu
1. pyqt4
		
		sudo apt-get install python-qt4
2. pyqt4-dev-tools

		sudo apt-get install pyqt4-dev-tools
3. qt4-designer
		
		sudo apt-get install python-qt4 qt4-designe
4. Google Translate Python Library
	
		pip3 install google-cloud-translate

#### Microsoft Windows
	Install Ubuntu on Workstation

## Files and Folder Tree

	/GUI
		/App
			/img
				/rit_logo.png
			/res
				/GCredentials.json
			/Application.ui
			/AppResources.qrc
			/GTranslate.py
			/Main.py
	/LICENSE
	/README.md

## Files and Folder Description

1. `/img` :  [Folder]
		Contains all the images for the UI

2. `/res` : [Folder]
		Contains Resources for Backend

3. `Application.ui` : (UI File - XML)
		A qt4 designer file which contains XML parsed UI description. Open this file using the command below
		
		qt4-designer Application.ui

4. `AppResources.qrc` : (Resources File - XML)
		A qt4 resource file which contains XML parsed Resources description. No effect if it is executed.

5. `GTranslate.py` : (Python Module)
		Python Module that contains Method to translate from English to Kannada

6. `Main.py` : (Python File)
		Main Application File. To start the Application use the command below
		
		python3 Main.py


## UI files to Python 
		
The `Application.ui` file has to be converted to Python to write backend in Python. To generate .`py` files from `.ui` files use the command given below. It is recommended to use the same command as given below.
	
	pyuic4 Application.ui -o Application.py

You can now see an `Application.py` file in your directory
Open the file and change the last line
	
	import AppResources_rc

to

	import AppResources

## Resources files to Python
All the images and other resources will be converted to appropriate format so as to use it in python code. To convert `.qrc` to `.py` use the command given below. It is recommended to use the same command as below.

	pyrcc4 AppResources.qrc -o AppResources.py -py3

You can now see a file named `AppResources.py` in your directory

## Starting the Application

Start the Application by typing in

	python3 Main.py

## License
MIT License

	Copyright (c) 2019 Shashank Sharma

	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in all
	copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
	SOFTWARE.

