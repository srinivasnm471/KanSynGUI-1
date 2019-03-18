#!/bin/sh
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
#
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
