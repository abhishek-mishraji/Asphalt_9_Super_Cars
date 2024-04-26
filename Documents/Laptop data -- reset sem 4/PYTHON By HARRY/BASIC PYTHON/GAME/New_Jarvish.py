import pyttsx3
import datetime
import speech_recognition as sr
# **************************
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# *******************


def wish():
    hour = int(datetime.datetime.now().hour)

    if(hour >= 0 and hour < 12):
        speak("GOod morninng")
    elif(hour >= 12 and hour < 18):
        speak("GOod Afternoon")
    else:
        speak("GOod Evening")

    speak("abhe sir. please tell me what is thee  work for today")
# ********************************************


def takecmd():
    # it take  voice input fromm user  and convert into string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio,)


# ***************************************************
if __name__ == "__main__":
    speak("wakingup Ai.")
    wish()
