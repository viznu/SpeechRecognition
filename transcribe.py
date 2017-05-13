import speech_recognition as sr
from os import path
import webbrowser

# User Input
option = raw_input("Choose Option:-\n1.Microphone Input\n2.Audio File Input\nEnter option :- ")
r = sr.Recognizer()
#audio = NULL

if int(option) == 1: 
	with sr.Microphone() as source:
    		print("Say something!")
    		audio = r.listen(source)

if int(option) == 2:
	AUDIO_FILE = raw_input("\nEnter File Path :- ")
	with sr.AudioFile(AUDIO_FILE) as source:
    		audio = r.record(source)

try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    text = r.recognize_google(audio)
    # test for URL format
    url = 'http://www.python.org/'
    # test for Google Search
    url1 = "https://www.google.com/search?q=" + text
    # opens URL
    webbrowser.open_new(url)
    # opens Google Search 
    webbrowser.open_new(url1)
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
