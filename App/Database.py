# -*- coding: utf-8 -*-
# =============================================================================
#Developer : 
#       Shashank Sharma(shashankrnr32@gmail.com)
# 
#Description : 
#       Database Implementation for Application. Uses JSON        
# =============================================================================

import json
import os
from scipy.io import wavfile as wav


item = {
        'wav_id' : '',
        'duration' : 0,
        'dsp' : True,
        'kan_txt' : ''
        }

class Database:
    
    def __init__(self,file_path = 'db.json'):
        
        self.DB = file_path
        self.wav_path = os.environ['WAVDIR']
        with open(file_path, 'r') as db:
            self.__data__ = json.load(db)
        self.__data__ = list(self.__data__)
        self.__server_length__ = len(self.__data__)
        
        
    def add_entry(self,kan_txt, wav_id, dsp = True,update = False):
        #======================================================================
        #Adds an entry to the database
        #======================================================================
        
        if dsp:
            fs,samples = wav.read('/{}/DSP/kan_{}.wav'.format(self.wav_path,wav_id))
        else:
            fs,samples = wav.read('{}/NoDSP/kan_{}.wav'.format(self.wav_path,wav_id))
        
        #Duration in seconds
        dur = len(samples)/fs
        
        entry = item.copy()
        entry['wav_id'] = wav_id
        entry['duration'] = dur
        entry['kan_txt'] = kan_txt
        
        #Add entry Locally
        self.__data__.append(entry)
        
        #Update JSON on request
        if update:
            self.update_database()
    
        
    def update_database(self):
        #======================================================================
        #Write into JSON File
        #======================================================================
        
        with open(self.DB, 'w') as db:
            json.dump(self.__data__, db)
        self.__server_length__ = len(self.__data__)
    
    
    def get_last_entry(self):
        #======================================================================
        #Returns the last entry of the database
        #======================================================================
        return self.__data__[-1]
    
    
    def get_all_txt(self):
        #======================================================================
        #Returns all the kannada text transcripts from the database
        #======================================================================
        txt_list = list()
        for x in self.__data__:
            txt_list.append(x['kan_txt'])
        else:
            return txt_list
    
        
        