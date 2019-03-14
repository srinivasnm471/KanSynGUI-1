# GUI Documentation

## Libraries Installation

### Linux/Ubuntu
**Recent Update** : `/run.sh` Handles Installation of Libraries

### Microsoft Windows
	Boot up Ubuntu

## Files and Folder Tree

	/GUI
		/App
			/img
			/res
				/GCredentials.json
				/db.txt
			/Application.ui
			/AppResources.qrc
			/GTranslate.py
			/FestAPI.sh
			/Main.py
			
		/LICENSE
		/README.md
		/run.sh

## Files and Folder Description

1. `/img` :  [Folder]
		Contains all the images and icons for the UI

2. `/res` : [Folder]
		Contains Resources for Backend

3. `Application.ui` : (UI File - XML)
		A qt4 designer file which contains XML parsed UI description. Open this file using the command below
		
		qt4-designer Application.ui

4. `AppResources.qrc` : (Resources File - XML)
		A qt4 resource file which contains XML parsed Resources description.

5. `GTranslate.py` : (Python Module)
		Python Module that contains Method to translate from English to Kannada

6. `Main.py` : (Python File)
		Main Application File. To start the Application use the command below
		
		python3 Main.py


## UI files to Python 

**Recent Update** : The `/run.sh` script handles the conversion now
		
## Resources files to Python

**Recent Update** : The `/run.sh` script handles the conversion now

## Building and Starting the Application

### Building the Application 

1. Open `App/Main.py` and checkout `setEnv()` function. Change the directory path as per your project. 
2. Run the command below

		chmod 755 ./run.sh

### Start the Application by typing in

	./run.sh

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
