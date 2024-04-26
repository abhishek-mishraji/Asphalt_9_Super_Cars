import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from datetime import date
import smtplib
import pyaudio
from translate import Translator
# ***************************************************
# ***************************************************
no = 0
i = 0


def called():
    # print("exception calledd ")
    global no
    no = 1


# **************************
engine = pyttsx3.init()
engine = pyttsx3.init('sapi5')  # "sapi5 --- convert text into speech"
voices = engine.getProperty('voices')
# for voice in voices:
# print(voice.id)
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)


def speak(audio):

    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate", 170)  # speech speed

    engine.say(audio)
    engine.runAndWait()
# **************


# **************


def error(audio):
    engine.say(audio)
    engine.runAndWait()  # it allow to system to say text
# *****************************************************************


def wish():
    hour = int(datetime.datetime.now().hour)

    if(hour >= 0 and hour < 12):
        speak("शुभ प्रभात")
    elif(hour >= 12 and hour < 18):
        speak("नमस्कार")
    else:
        speak("सुसंध्या")

    speak("अभी महोदय,कृपया मुझे बताएं कि आज के लिए क्या काम है")
# ********************************************


def sendEmail(to, content):
    # use to send mail to any  machine
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kbhi87033@gmail.com', '@@abhishek@@')
    server.sendmail('kbhi87033@gmail.com', to, content)
    server.close()
# ******************************************************************


def takecmd():
    # it take  voice input fromm user  and convert into string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.energy_threshold = 400  # how louder u want say
        r.pause_threshold = 1  # kitne der ruke  fir uske baad apna kaam kare
        audio = r.listen(source)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='hi')
        print(f"User said : {query} \n")

    except Exception as e:

        called()
        # print(e)
        # error("Please say again again: ")
        # print("Please say again again: \n")
        return "None"
    return query


# **************************************************
# ***************************************************
if __name__ == "__main__":

    # takecmd()

    while True:
        # query = takecmd().lower()
        query = takecmd()
        if "उठो" in query:
            while True:
                if i == 0:
                    speak("कल्पना आपके लिए तैयार है")
                    wish()
                    i = i+1
                query = takecmd()
                #  All tasks........................
                # *********************************
                if "विकिपीडिया" in query:
                    speak("विकिपीडिया की खोज में .........")
                    query = query.replace("विकिपीडिया", "")
                    wikipedia.set_lang("hi")
                    results = wikipedia.summary(query, sentences=1)

                    speak("विकिपीडिया के अनुसार.....")

                    print(results)
                    speak(results)
                # ***************
                elif "यूट्यूब खोलें" in query:
                    speak("यूट्यूब ओपनिंग")
                    webbrowser.open("youtube.com")
                # *****************
                elif "open google" in query:
                    speak("opening google")
                    webbrowser.open("google.com")
                # *******************
                elif "open stack overflow" in query:
                    speak("opening stack overflow")
                    webbrowser.open("stackoverflow.com")
                # *********************

                elif 'play music' in query:
                    speak("playing music")
                    music_dir = 'C:\\Users\\abhia\\Documents\\PYTHON By HARRY\\Music'
                    songs = os.listdir(music_dir)
                    # print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif 'time' in query:
                    strtime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"The time is {strtime}")

                elif "month" in query:
                    strtime = datetime.datetime.now().strftime("%h:%m")
                    speak(f"The month is {strtime}")
                elif "year" in query:
                    current_year = date.today().year
                    speak(f"the year is {current_year}")

                elif "open vs code" in query:
                    path = "C:\\Users\\abhia\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(path)

                elif "sleep" in query:
                    speak("i am going to sleep")
                    quit()

                elif 'email' in query:
                    try:
                        speak("What should I say?")
                        content = takecmd()
                        to = "abhiabhishek2714@gmail.com"
                        sendEmail(to, content)
                        speak("Email has been sent!")

                    except Exception as e:
                        print(e)
                        speak(
                            "Sorry my friend harry bhai. I am not able to send this email")
                else:
                    if(no == 0):
                        print("Please say again  ...... \n")
                        error("Please say again : ")
