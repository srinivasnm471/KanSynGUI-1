# -*- coding: utf-8 -*-
# =============================================================================
# Developer : Shashank Sharma
# Description : 
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