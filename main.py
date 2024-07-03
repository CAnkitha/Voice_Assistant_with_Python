import pyttsx3 as p
import speech_recognition as sr
from web import *
from YT_audio import *
from News import *
import randfacts
from jokes import *
from weather import *
import datetime


engine=p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',130)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# print(voices)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishes():
    hour=int(datetime.datetime.now().hour)
    if(hour>0 and hour<12):
        return("morning")
    elif (hour > 12 and hour < 16):
        return ("afternoon")
    else:
        return ("evening")




today_date=datetime.datetime.now()
r = sr.Recognizer()
speak("Hello Ankitha good " + wishes() + "I am your voice assistant ")
speak("how can i help u")

with sr.Microphone() as source:
    r.energy_threshold=2000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("you need information related to which topic")

    with sr.Microphone() as source:
        r.energy_threshold = 2000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("searching for {} in wikipedia".format(infor))
    print("searching for {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)
    input("Press Enter to close the browser...")


elif "play" and "video" in text2:
    speak("you want me to play which video")
    with sr.Microphone() as source:
        r.energy_threshold=2000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    print("playing {} on youtube".format(vid))
    speak("playing {} on youtube".format(vid))
    assist=Music()
    assist.play(vid)

elif "news" in text2:
    arr=news()
    speak("Sure Ankitha. I will read the news for u")
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" in text2:
    speak("Sure Ankitha. I will tell a fact for u")
    x = randfacts.get_fact()
    print(x)
    speak(x)

elif "joke" in text2 :
    print("Sure Ankitha. I will tell a joke for u")
    speak("Sure Ankitha. I will tell a joke for u")
    arr = joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])

elif "temperature" in text2 :
    temperature = temp()
    description = desc()
    weather_info = f"Temperature in Kurnool is {temperature} degrees Celsius with {description}."
    print(weather_info)
    speak(weather_info)


elif "date" in text2 or "time" in text2:
    now = datetime.datetime.now().strftime("%B %d, %Y and currently the time is %I:%M %p")
    date_info = f"Today is {now}."
    print(date_info)
    speak(date_info)
