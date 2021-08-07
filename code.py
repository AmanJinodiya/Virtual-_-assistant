from logging import exception
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
from requests import get
import json
import sys
from pytube import YouTube

import pywhatkit as kit
import pyautogui as pg





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good morning sir")
    elif hour >= 12 and hour<18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    query = query.lower()
    return query

def task_execution():
    
    while True:
        query = takeCommand().lower()
        if 'hello ' in query:
            speak("oo,hello sir ")

        if 'wikipedia' in query:
            speak("wait sir I am serching")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open guruji' in query or 'sensei' in query or 'sensor' in query or 'open youtube' in query:
            webbrowser.open("youtube.com")

        

        elif 'bus' in query:
            webbrowser.open("http://www.charteredbus.in/search-results")
        
        # elif 'play song on youtube' in query or 'onilne songs' in query:
        #     song = takeCommand().lower()
        #     kit.playonyt(f"{song}")


        
        elif 'open google' in query:
            speak("sir, What should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")



        elif 'download youtube video' in query:
            try:
                speak("Enter your link here")
                link = input("Enter your link here")
                url = YouTube(link)
                speak("Downlodind.....")
                video = url.streams.first()
                video.download()
                speak("downloaded !")
                print("downloaded !")
            except exception as e:
                speak("Some error sir try again")
        
        elif 'open new tab' in query:
            webbrowser.open_new("google.com")

        
        elif 'play music' in query or 'play some music' in query:
            music_add = 'F:\\music'
            songs = os.listdir(music_add)
            print(songs)
            i = random.randint(1,50)
            os.startfile(os.path.join(music_add,songs[i]))
        
        elif 'time ' in query or  'kitne baje ' in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"sir now time is {time}")
        
        elif 'open code' in query or 'code banate ' in query or 'open vs' in query:
            code_add = "C:\\Users\\amanj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_add)
        
        elif 'close code' in query or 'shut that shit ' in query or 'close vs' in query:
            speak("Ok sir , closing vs code ")
            os.system("taskkill /f /im code.exe")


        elif 'open notepad' in query or 'notes' in query or 'open np' in query:
            n_add = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(n_add)

        elif 'close notepad' in query:
            speak("closeing notepad sir.")
            os.system("taskkill /f /in notepad.exe")
        
        elif 'open word' in query or 'MS word' in query:
            m_add = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(m_add)
        
        elif 'openbravo' in query or 'secret browser' in query:
            b_add ="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(m_add)

        elif 'open pycharm' in query :
            p_add = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.2\\bin\\pycharm64.exe"
            os.startfile(p_add)

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
        
        elif 'shut down pc' in query:
            os.system("shoutdown /s /t s")

        elif 'restart pc' in query:
            os.system("shoutdown /r /t s")
        
        
        elif 'sleep the pc' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        # elif 'switch the window' in query:
        #     pyautogui.keyDown("alt")
        #     pyautogui.press("tab")
        #     time.sleep(1)
        #     pyautogui.keyUp("alt")

        # elif 'take screenshot' in query or 'save it for future' in query:
        #     speak("sir, please tell me the name for this screenshot")
        #     name = takeCommand().lower()
        #     speak("please sir hold the screen for few seconds, I am taking the screenshot")
        #     img= pyautogui.screenshot()
        #     img.save(f"{name}.png")
        #     speak("Done sir ,I tooked it")

        elif 'now go to sleep' in query:
            speak("ok sir Wake me up, I am there for you, I am not like your exes")
            sys.exit()
        
        elif 'take rest' in query:
            speak("Ok sir, by")
            sys.exit()
        
        elif 'take a break' in query:
            speak("Ok sir \n Have a sweet day")
            sys.exit()

"""***************************************************************************************************************************************"""
if __name__ == "__main__":
    wake_jarvis = takeCommand()

    if 'wake up' in wake_jarvis:
        wishme()
        speak("\n hope your day is fine, tell me ...")
        task_execution()

    elif 'now go to sleep' in wake_jarvis:
        speak("ok sir Wake me up, I am there for you, I am not like your exes")
        sys.exit()
        
    elif 'take rest' in wake_jarvis:
        speak("Ok sir, by")
        sys.exit()
        
    elif 'take a break' in wake_jarvis:
        speak("Ok sir \n Have a sweet day")
        sys.exit()
    

    