"""
Created on Tue Feb 23 20:41:00 2021
@author: sandhu
"""
#import TKinter
import speech_recognition as sr
#import pyttsx3
import playsound
from gtts import gTTS
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
#from ecapture import ecapture as ec
import wolframalpha
#import json
import requests
#from _ctypes import Union, Structure, Array
from kivy.app import App
from kivy.uix.button import Button


print("आपकी SSP सहायता अब सक्षम है")

# engine=pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
# engine.setProperty('rate', 150)
# print('\n voice',voices[1].id)


# def speak(text):
#    engine.say(text)
#    engine.runAndWait()


num = 0                         
def speak(output): 
	global num 

	# num to rename every audio file 
	# with different name to remove ambiguity 
	num += 1
	print("PerSon : ", output) 

	toSpeak = gTTS(text = output, lang ='hi', slow = True) 
	# saving the audio file given by google text to speech 
	file = str(num)+".mp3"
	toSpeak.save(file) 
	
	# playsound package is used to play the same file. 
	playsound.playsound(file, True) 
	os.remove(file) 



def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("\n Hello,Good Morning")
        print("\n Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("\n Hello,Good Afternoon")
        print("\n Hello,Good Afternoon")
    else:
        speak("\n Hello,Good Evening   होर सुनाओ ")
        print("\n Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("\n Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("I don't understand what are you saying, please say that again")
            return "None"
        return statement

speak("आपकी SSP सहायता अब सक्षम है")
wishMe()


if __name__ == "__main__":
    while True:
        speak("Tell me how can I help you now?")
        
        statement = takeCommand().lower()
        if statement==0:
            continue
        break
    if "good bye" in statement or "ok bye" in statement or "stop" in statement or "ok then you cant help me" in statement or "that was shit, you cant helping" in statement or "quit" in statement or "you can't help me " in statement or "neither of these" in statement or "stop, i don't want to continue" in statement or "you can't help me with what i need" in statement or "i guess you can't help me" in statement or "leave it" in statement or "leave it please" in statement or "leave that" in statement or "leave this" in statement or "i don't want to" in statement or "that's not what i want" in statement or "ok, but that doesnt help me" in statement or "stop go back" in statement or "do you get anything?" in statement or "nothing else?" in statement or "stop," in statement or "stop there" in statement or "okey, stop" in statement or "terminate it" in statement or "stop it" in statement or "exit" in statement or "exit please" in statement or "quit please" in statement or "exit from this" in statement or "quit" in statement or "i want to quit" in statement :
        
        speak('your S.S.P assistant is shutting down,Good bye')
        print('your S.S.P assistant is shutting down,Good bye')
    #    break



    if 'wikipedia' in statement:
        speak('Searching Wikipedia...')
        statement =statement.replace("wikipedia", "")
        results = wikipedia.summary(statement, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in statement:
        webbrowser.open_new_tab("https://www.youtube.com")
        speak("youtube is open now")
        time.sleep(5)

    elif 'open google' in statement:
        webbrowser.open_new_tab("https://www.google.com")
        speak("Google chrome is open now")
        time.sleep(5)

    elif 'open gmail' in statement:
        webbrowser.open_new_tab("gmail.com")
        speak("Google Mail open now")
        time.sleep(5)

    elif "weather" in statement:
        api_key="8ef61edcf1c576d65d836254e11ea420"
        base_url="https://api.openweathermap.org/data/2.5/weather?"
        speak("whats the city name")
        city_name=takeCommand()
        complete_url=base_url+"appid="+api_key+"&q="+city_name
        response = requests.get(complete_url)
        x=response.json()
        if x["cod"]!="404":
            y=x["main"]
            current_temperature = y["temp"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak(" Temperature in kelvin unit is " +
                  str(current_temperature) +
                  "\n humidity in percentage is " +
                  str(current_humidiy) +
                  "\n description  " +
                  str(weather_description))
            print(" Temperature in kelvin unit = " +
                  str(current_temperature) +
                  "\n humidity (in percentage) = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_description))

        else:
            speak(" City Not Found ")



    elif 'time' in statement:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")

    elif 'who are you' in statement or 'what can you do' in statement:
        speak('I am S.S.P version 1 point O your persoanl assistant. I am programmed to minor tasks like'
              'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
              'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


    elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
        speak("I was built by Sharandeep Singh")
        print("I was built by Sharandeep Singh")

    elif "open stackoverflow" in statement:
        webbrowser.open_new_tab("https://stackoverflow.com/login")
        speak("Here is stackoverflow")

    elif 'news' in statement:
        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        speak('Here are some headlines from the Times of India,Happy reading')
        time.sleep(6)

    elif "camera" in statement or "take a photo" in statement:
        ec.capture(0,"robo camera","img.jpg")

    elif 'search'  in statement:
        statement = statement.replace("search", "")
        webbrowser.open_new_tab(statement)
        time.sleep(5)

    elif 'ask' in statement:
        speak('I can answer to computational and geographical questions and what question do you want to ask now')
        question=takeCommand()
        app_id="UTPHRH-PU446TQWP5"
        client = wolframalpha.Client('UTPHRH-PU446TQWP5')
        res = client.query(question)
        answer = next(res.results).text
        speak(answer)
        print(answer)


    elif "log off" in statement or "sign out" in statement:
        speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
        subprocess.call(["shutdown", "/l"])
#agee ma karo
time.sleep(3)
# pip install 
