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
# =============================================================================

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
