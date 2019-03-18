# -*- coding: utf-8 -*-

# =============================================================================
#Developer : Shashank Sharma
# 
#Description : 
#     Google Translate API Implementation
#     Needs an Internet Connection
# =============================================================================

from google.cloud import translate
import os

#Path to Private Key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getcwd() + '/res/GCredentials.json'

def en2kn(text):
    client = translate.Client()
    res = client.translate(text, source_language='en',target_language = 'kn')
    return res['translatedText']


# =============================================================================
#Developer : 
#       Shashank Sharma(shashankrnr32@gmail.com)
# 
#Description : 
#       Database Implementation for Application. Uses SQLite       
# =============================================================================

import sqlite3
from scipy.io import wavfile as wav

class Database:
    
    def __init__(self,database = 'res/DB'):
        
        self.wav_path = os.environ['WAVDIR']
        
        #Establish Connection to DB
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        
    def get_last_entry(self):
        #======================================================================
        #Retrieves The Last Entry of the Database
        #======================================================================
        entry = self.cursor.execute('SELECT * FROM kan WHERE   id = (SELECT MAX(id) FROM kan);')
        return list(entry)
            
        
        
    def add_entry(self,kan_txt, wav_id, dsp = True, reverse_id = -1):
        #======================================================================
        #Adds an entry to the database
        #======================================================================
        
        #Read File and determine Duration of the Wave File
        if dsp:
            fs,samples = wav.read('/{}/DSP/kan_{}.wav'.format(self.wav_path,wav_id))
        else:
            fs,samples = wav.read('{}/NoDSP/kan_{}.wav'.format(self.wav_path,wav_id))
        
        #Duration in seconds
        dur = len(samples)/fs
        
        #Insert into Database
        self.cursor.execute('INSERT INTO kan(wav_id,txt,dsp,duration,reverse_id) VALUES (?,?,?,?,?)', (wav_id, kan_txt, int(dsp), dur, reverse_id))
        
        #Add Reverse ID to the reverse entry
        if reverse_id != -1:
            self.cursor.execute('UPDATE kan SET reverse_id = ? WHERE wav_id = ?',(wav_id, reverse_id))
        
        #Commit Changes
        self.conn.commit()
        