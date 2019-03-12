#!/bin/sh
#==============================================================================
#Developer : 
#
#	Varun S S(varunsridhar614@gmail.com)
#
#Description : 
#
#	Shell API to call Festvox Project.
#	Appropriate Permissions to be given before Building Project.
#	This Shell Script is called by synthesize() method of Main.py
#
#Instruction:
#
#	Create a directory tree as given below
#	Project/
#		|--WavFiles/
#			|--NoDSP
#			|--DSP
#
#Directory:
#
#	GUI/App/FestAPI.sh
#
#Production Code and Documentation : 
#
#	Shashank Sharma(shashankrnr32@gmail.com)
#
#==============================================================================

#Run TTS from Festvox Project
cd $PRODIR
./bin/do_clustergen cg_test tts tts etc/temp.txt
sleep 5
rm etc/temp.txt
mv $PRODIR/test/tts/kan_$2.wav ~/Project/WavFiles/NoDSP/

#DSP -Digital Signal Processing Operations
#
#==============================================================================
#Noise Removal using SOX
#https://en.wikipedia.org/wiki/SoX






#==============================================================================
#
#
#
#==============================================================================
#Pitch Shift using soundstretch
#http://www.surina.net/soundtouch/

b="$1"
a="1"
if [ "$b" -eq "$a" ]
then
	soundstretch ~/Project/WavFiles/NoDSP/kan_$2.wav ~/Project/WavFiles/DSP/kan_$2.wav -pitch=+4.5
fi

#==============================================================================
