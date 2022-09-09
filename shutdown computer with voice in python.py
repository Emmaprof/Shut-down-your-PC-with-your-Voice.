import  os, pyttsx3
import speech_recognition as sr

""" Function of recognizing sounds"""

def take_commands():
    """ Recognizing speech recognition models"""
    r = sr.Recognizer()
    """ Opening our microphones """
    with sr.Microphone() as source:
        print("Listening now")
        r.phrase_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio)
            print("the query is =", Query)
        except Exception as e:
            print(e)
            print('say that again EMMANUEL')
            return "None"
        import time
        time.sleep(2)
        return Query

def Speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


Speak("DO you want to shutdown your computer EMMANUEL?")

while True:
    command = take_commands()


    if "exit" in command:
        Speak("OK EMMANUEL, let me exit")
        break
    if "yes" in command:
        Speak("OK EMMANUEL thank you computer will be shutdown now" )
        os.system("shutdown /s /t 30")
    if "no" in command:
        Speak("OK EMMANUEL, no problem")

        break 