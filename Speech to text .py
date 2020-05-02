# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:18:24 2020

@author: Puruboii
"""


import speech_recognition as sr

path = r"C:\Users\Anonymous\Desktop\Untitled.wav"

A_F = (path)

#use audio file as source 

r = sr.Recognizer() # initialise recogniser

with sr.AudioFile(A_F) as source :
    audio = r.record(source)   # reads audio file 
    
    try:
        print("audio file contents "+r.recognize_google(audio))
        
    except sr.UnkonwnValueError:
        print("google recogniser could not read the audio")
    
    except sr.RequestError() :
        print("couldnt get results from google recogniser")
    
