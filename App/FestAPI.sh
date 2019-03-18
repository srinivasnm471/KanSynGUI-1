#!/bin/sh

# =============================================================================
# Copyright (c) 2019 Shashank Sharma
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
# =============================================================================

#==============================================================================
#Developer : 
#
#	Primary Code :Varun S S(varunsridhar614@gmail.com)
#	Production Code : Shashank Sharma(shashankrnr32@gmail.com)
#
#Description : 
#
#	Shell API to call Festvox Project.
#	Appropriate Permissions to be given before Building Project.
#	This Shell Script is called by synthesize() method of Main.py
#
#==============================================================================

#Run TTS from Festvox Project
cd $PRODIR
./bin/do_clustergen cg_test tts tts etc/temp.txt
#sleep 5
rm etc/temp.txt
mv $PRODIR/test/tts/kan_$2.wav ~/Project/GUI/WavFiles/NoDSP/

#DSP -Digital Signal Processing Operations

#==============================================================================
#Noise Removal using SOX
#https://en.wikipedia.org/wiki/SoX






#==============================================================================



#==============================================================================
#Pitch Shift using soundstretch
#http://www.surina.net/soundtouch/

b="$1"
a="1"
if [ "$b" -eq "$a" ]
then
	soundstretch ~/Project/GUI/WavFiles/NoDSP/kan_$2.wav ~/Project/GUI/WavFiles/DSP/kan_$2.wav -pitch=+4.5
fi

#==============================================================================
