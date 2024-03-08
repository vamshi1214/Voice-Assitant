import speech_recognition as sr
import pyttsx3
import pyaudio
import webbrowser
import datetime
import pyjokes
import smtplib
import os
import wikipedia
import random
import openai
from urllib.request import urlopen
from tkinter import *
openai.api_key="***************API************************"
completion=openai.Completion()
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
x=random.randint(1,36)
def gui():
    root =Tk()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def Reply(question):
    prompt=f'vamshi: {question}\n ahkkel: '
    response=completion.create(prompt=prompt, engine="text-davinci-003", stop=['\Ahkkel'], max_tokens=400)
    answer=response.choices[0].text.strip()
    return answer
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("ahkkel")
    speak("I am your Assistant")
    speak(assname)
    speak("how can i help you")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reognizing.....")
        query=r.recognize_google(audio,language="en-in")
        print(f"you said : {query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return ""
    return query
'''def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id','your email password')
    server.sendmail('your email id', to, content)
    server.close()
sendemail("nagulavamshi1214@gmail.com","hello")'''
if _name_ == '_main_':
    clear = lambda: os.system('cls')
    clear()
    wishme()
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak("searching in wikipedia.....")
            quer=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            speak("here you go to the youtube\n")
            webbrowser.open("youtube.com")
        elif "open google" in query:
            speak("here you go to the google\n")
            webbrowser.open("google.com")
        elif "play music" in query or "play some music" in query or "play songs" in query:
            speak("here you go with music")
            music_dir = "C:\\Users\\lenovo\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[x]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "hi akhil" in query or "hey akhil" in query or "hello akhil" in query:
            speak("Hello sir")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        elif "what's your name" in query or "what is your name" in query:
            speak(f"my name is ahkkel. created by nagula vamshi goud for his project")
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Vamshi as a project ,my name is the reverse of one of vamshi's friend,There will be many improvements as the time goes.")
        elif "updates" in query or "upgrades" in query or "upgrade" in query:
            speak("yeah there will be many updates coming up as the time goes on and the most exciting thing is\
             that i will be upgraded with graphical user interface")
        elif 'joke' in query:
            speak("here you go")
            speak(pyjokes.get_joke())
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)
        elif "who are you" in query:
            speak("I am your virtual assistant created by nagula vamshi goud, my name is the reverse of one of vamshi's friend")
        elif 'reason for your creation' in query or 'purpose for your creation' in query:
            speak("I was created as a project by Mister nagula vamshi goud")
        elif "where is" in query or "locate" in query:
            query = query.replace("where is", "")
            location = query
            speak("you asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")
        elif "weather" in query:
            ans = Reply(query)
            print(ans)
            speak(ans)
        elif "bye" in query or "exit" in query:
            speak("thank you sir for your wonderful time. I am here to serve you anytime")
            break
        else:
            ans = Reply(query)
            print(ans)
            speak(ans)