import pyttsx3 
import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True: 
    text = input("Enter some text to convert into speech ")
    speak(text)

def time():
    Time= datetime.datetime.now().strftime()("%I:%M:%S") # Hour = I, Min = M, Sec = S
    speak("the current time is:")
    speak(Time)

time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is : ")
    speak(date)
    speak(month)
    speak(year)

date()

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <18:
        speak("Good Evening Sir!")
    elif hour >= 18 and hour <24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

greeting()
    
def wishme():
    speak("Welcome Back Sir!")
    time()
    date()
    greeting()
    speak("Jarvis at your service, please tell me how i can help you?")

wishme()

def takeCommandCMD():
    query= input("please tell me how i can help you\n")
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query=takeCommandCMD().lower()
        if 'time' in query:
            time()
        elif 'date' in query
            date()