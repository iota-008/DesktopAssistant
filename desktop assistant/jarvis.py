import pyttsx3
import datetime
import string
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui as pag
import psutil
import pyjokes

engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('voices',voice[0].id)
newVoiceRate = 200
engine.setProperty('rate',newVoiceRate)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def SayJoke():
    speak(pyjokes.get_joke())

def cpu():
    usage = str(psutil.cpu_percent())
    battery = psutil.sensors_battery()
    speak("cpu utilization is" + usage + "and" + "battery percentage is" + battery.percent)

def TakeScreenshot():
    img = pag.screenshot()
    img.save(r"C:\Users\iota\Pictures\test")


def SendMail(to, context):
    server = smtplib.SMPTP('smpt.google.com', 587)
    server.ehlo()
    server.starttls()
    server.login('raiboleankit8@gmail.com', 'ankitraibole008@123')
    server.sendmail('raiboleankit8@gmail.com', to, context)
    server.close()


def SayDate():
    speak( SayTime() +"today is"+ datetime.datetime.now().strftime("%A") )

def SayTime():
    hours = int(datetime.datetime.now().strftime("%H"))
    minutes = int(datetime.datetime.now().strftime("%M"))
    seconds = int(datetime.datetime.now().strftime("%S"))
    greet = " "
    if hours >= 6 and hours <12:
        greet = "good morning."
    elif hours >= 12 and hours < 17:
        greet = "good afternoon."
    elif hours >= 17 and hours < 22:
        greet = "good evening."
    elif hours >= 24 and hours < 6:
        greet = "you should sleep now,good night."
                
    t = greet + "current time is " + str(hours) + "hours" + str(minutes) + "minute" + str(seconds) +  "seconds"
    return t

def wishme():
    speak("hello sir, welcome back")
    
    

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language="en=IN")
        print(query)
        
    except Exception as e:
        print(e)
        speak("Say that Again Please...")
        return "None"
    return query

    
if __name__ == "__main__":

    wishme()

    while True:
        query = TakeCommand().lower()
        print(query)

        if "time" in query:
            SayTime()
            
        elif "date" in query:
            SayDate()

        elif "offline" in query:
            exit()

        elif "wikipedia" in query:
            speak("searching on wikipedia....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)

        elif "send mail" in query:
            try:
                speak("say the reciever email id please ")
                to = TakeCommand()
                
                speak("what should i send....")
                context = TakeCommand()
                SendMail(to, context)
            except Exception as e:
                speak(e)
                speak("sorry unable to send the mail")

        elif "search in chrome" in query:
            speak("what should i search..")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = TakeCommand().lower
            wb.get(chromepath).open_new_tab(search + ".com")

        elif "logout" in query:
            os.system("shutdown - l")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play songs" in query:
            location = "D:\Letest New song"
            songs = os.listdir(location)
            os.startfile(os.path.join(location, songs[0]))

        elif "remember that" in query:
            speak("what should i remember")
            data = TakeCommand()
            speak("you asked me to remember that" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "what you remember" in query:
            file = open("data.txt", "r")
            data = file.read()
            speak("you asked me to remember that" + data)

        elif "screenshot" in query:
            TakeScreenshot()
            speak("image saved in test folder in photos")

        elif "cpu" in query:
            cpu()
            
        elif "jokes" in query:
            SayJoke()

        else:
            pass

