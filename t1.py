# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 20:43:23 2019

@author: AKASH
"""

import pyttsx3 #pip install
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    elif hour>=18 and hour<21:
        print("Good Evening")
        speak("Good Evening")

    else:
        print("Good Evening")
        speak("Good Evening")  
    print("I am zeni Sir. Please tell me how may I help you")
    speak("I am zeni, Sir. Please tell me how may I help you")       

'''def takeCommand():
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
    return query
'''
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email@gmail.com', 'password')
    server.sendmail('email@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        print("Say: ")
        query=str(input())
        ##query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'i have a doubt' in query:
            print('What is your doubt about sir ?')
            speak('whatis your doubt, about sir')
            print('Type/Speak your doubt: ')
            a=str(input())
            print("searching ....");
            print(wikipedia.summary(a, sentences=1))
            speak(wikipedia.summary(a, sentences=1))
            ##webbrowser.open('wikipedia.com\',search) 
            ##query = query.replace("wikipedia", "")
            ##results = wikipedia.summary(query, sentences=2)
            ##speak("According to Wikipedia")
            ##print(results)
            ##speak(results)

        elif 'open youtube' in query:
            print("Aah just a second sir !!")
            speak('aah just a second sir')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            print("Aah just a second sir !!")
            speak('aah just a second sir')
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            print("Aah just a second sir !!")
            speak('aah just a second sir')
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            print("Aah just a second sir !!")
            speak('aah just a second sir')
            music_dir = 'E:\S-O-N-G'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            print("Its a secret sorry!! ")
            speak("Its a secret sorry!! ")
            ##codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            ##os.startfile(codePath)

        elif 'email to nikhil' in query:
            try:
                print("What should I say?")
                speak("What should I say?")
                content=str(input())
                ##content = takeCommand()
                to = "nikhildesai1333@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("Sorry my friend akash bhai. I am not able to send this email")
                speak("Sorry my friend akash bhai. I am not able to send this email") 

        elif 'how are you' in query:
            print('happy as always ')
            speak('happy as always ')
            
        elif 'had dinner' in query:
            print('I dont eat, i just like to help  ')
            speak('i dont eat, i just like to help ')
            
        elif 'tell me a joke' in query:
            print('john: hey girl! call me a taxi \njin: yes, obviously you are a taxi.  ')
            speak('joth says. hey girl, call me a taxi. jin replies. yes, obviously. you are a taxi. hahaha !')    
            print("want one more\nY/N")
            speak("want one more")
            an=str(input())
            ans=an.lower()
            if 'y' in ans:
                print('If vegetarians eat vegetables, then what do humanitarians eat')
                speak('If vegetarians eat vegetables, then what do humanitarians eat')
            else:
                print('okay')
                speak("okay")
    
        elif 'bye' in query:
            print('Happy to help you sir BYE !! ')
            speak('happy to help you sir, bye ')
            print('exiting...')
            break
            exit()

        else:
             print('didnt got it sir ')
             speak('didnt got it sir ')
sys.exit()
