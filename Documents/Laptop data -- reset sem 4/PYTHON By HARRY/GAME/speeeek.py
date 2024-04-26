import pyttsx3
from translate import Translator
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from datetime import date
import smtplib
import pyaudio


engine = pyttsx3.init()

engine = pyttsx3.init('sapi5')  # "sapi5 --- convert text into speech"
voices = engine.getProperty('voices')
# *****************************


def speak(audio):

    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate", 170)  # speech speed

    engine.say(audio)
    engine.runAndWait()
    # *********************************


def wikispeek(audio):
    # translator = Translator(to_lang="hindi")
    # translation = translator.translate(audio)
    # audio.wikipedia.get_translation(audio)
    # engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate", 170)  # speech speed
    engine.say(audio)
    engine.runAndWait()


# **********************************
# for voice in voices:
#     print(voice.id)
# *************************
# translator = Translator(from_lang="english", to_lang="hindi")
# translation = translator.translate("Listening")
# engine.setProperty('voice', voices[1].id)
# print(translation)
# engine.say(translation)
# engine.say(translation)
# engine.runAndWait()
# *********************************
if __name__ == "__main__":
    query = " पी एम विकिपीडिया"
    if "विकिपीडिया" in query:
        speak("विकिपीडिया की खोज में .........")
        query = query.replace("विकिपीडिया", "")
        wikipedia.set_lang("hi")
        results = wikipedia.summary(query, sentences=2)

        speak("विकिपीडिया के अनुसार.....")

        print(results)
        wikispeek(results)
