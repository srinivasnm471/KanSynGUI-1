# -*- coding: utf-8 -*-

# =============================================================================
# Developer : Shashank Sharma
# Description : 
#     Google Translate API Implementation
#     Needs an Internet Connection
# 
# =============================================================================

from google.cloud import translate
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getcwd() + '/res/GCredentials.json'
def en2kn(text):    
    client = translate.Client()
    #x = client.get_languages()
    res = client.translate(text, source_language='en',target_language = 'kn')
    #print(res['translatedText'])
    return res['translatedText']