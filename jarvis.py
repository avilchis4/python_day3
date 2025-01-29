import pyttsx3 #pip install pyttsx3 == it is used to coverty text to speech
import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say("pyttsx3 it is used to convery text to speech")
    engine.runAndWait 

while True: 
    text = input("Enter some text to convert into speech")
    speak(text)

def time():
    Time= datetime.datetime.now().strftime()("%I:%M:%S") # Hour = I, Min = M, Sec = S
    speak("the current time is:")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is : ")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <18:
        speak("Good Evening Sir!")
    elif hour >= 18 and hour <24:
        speak("Good Evening Sir!")
    