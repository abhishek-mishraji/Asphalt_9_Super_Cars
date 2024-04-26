import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
no = 0


def called():
    # print("exception calledd ")
    global no
    no = 1


# **************************
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
# print(voices[1].id)


def speak(audio):
    engine.setProperty("rate", 170)
    engine.say(audio)
    engine.runAndWait()
# **************


def error(audio):
    engine.say(audio)
    engine.runAndWait()
# *****************************************************************


def wish():
    hour = int(datetime.datetime.now().hour)

    if(hour >= 0 and hour < 12):
        speak("GOod morninng")
    elif(hour >= 12 and hour < 18):
        speak("GOod Afternoon")
    else:
        speak("GOod Evening")

    speak("abhe sir, please tell me what is thee  work for today")
# ********************************************
# ******************************************************************


def takecmd():
    # it take  voice input fromm user  and convert into string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.energy_threshold = 300
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"U said : {query} \n")

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
    i = 0
    try:
        while True:
            query = takecmd().lower()
            if "wake up" in query:
                if i == 0:
                    speak("Wakingup   jarvish.  ")
                    wish()
                    i = i+1
                    query = takecmd().lower()

#       All tasks........................
# *     ***************************************************************************************
# #      Haal chaal
# *     **************************************************************************************
                if "how are you" in query:
                    speak("i am good sir, what about you")
                    query = takecmd().lower()
                    if "great" in query:
                        speak("that's fantastic")
                        query = takecmd().lower()
                        if "ask about" in query:
                            speak(
                                "oh! so sorry sir, please tell me how's your big brother's like intellegent shikha sis ,     awesome   diksha sis,   bhai and best guider varsha sis")

                            # ****************************
                            query = takecmd().lower()

                            if ("shikha") in query or ("diksha") in query or ("varun") in query or ("varsha") in query:
                                speak("hmmm! that's great")
                                if "shikha" not in query:
                                    speak("and, what about shikha")
                                if "diksha" not in query:
                                    speak("and, what about diksha")
                                if "varun" not in query:
                                    speak("and, what about varun")
                                if "varsha" not in query:
                                    speak("and, what about  varsha")
                            elif "not ok" in query:
                                speak(
                                    "i can't beleive, u  all not enjoying your life")

                            else:
                                if(no == 0):
                                    print("Please say again  ...... \n")
                                    error("Please say again : ")
                    elif "not ok" in query:
                        speak(
                            "what happened, sir please tell, i will do my best for u")
                    else:
                        if(no == 0):
                            print("Please say again  ...... \n")
                            error("Please say again : ")
                # ****************************************************************************************

#       ***********************************************************************

 #      ****************************************************************************

            elif "wikipedia" in query:
                speak("Searchin wikipedia.........")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia.....")
                print(results)
                speak(results)
            # ***************
            elif "open youtube" in query:
                speak("opening utube")
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

            elif "sleep" in query:
                    speak("i am going to sleep")
                    quit()    

            else:
                if(no == 0):
                    print("Please say again  ...... \n")
                    error("Please say again : ")
    except Exception as e:
        print("again")
