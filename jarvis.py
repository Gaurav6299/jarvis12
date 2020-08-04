import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
# import pass
import smtplib
import sys
import pyautogui
import psutil
import tkinter as tk
import wmi  # windows management instrumentations
import ctypes
from PyDictionary import PyDictionary
import calendar

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('rate', 130)
engine.setProperty('voice', voices[1].id)


# volume=engine.getProperty('volume')
# print(volume)
# engine.setProperty('volume',1)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    '''
    Here we doing use wish command for different time zone
  jarvis say time to time according to their original time
   '''

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(" Good  morning, Sir")
    elif hour >= 12 and hour < 18:
        speak(" Good  afternoon, Sir")
    else:
        speak(" Good  evening, Sir")

    speak(" All  system have been started, Now i am in online")
    speak(" Hello I am jarvis sir,I am your virtual assistant, please tell me how may i help you")
    # speak("The current temperature of this city is  32 degree celcious ")
    # speak("Please tell me How may I help you")


def command():
    # Here we are using command method to take the commad from the user.
    # What user actually say to jarvis.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        # r.energy_threshold=500
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said:{query}\n")

    except Exception as e:
        print("say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("kumargaurav6299@gmail.com", "7667268671")
    server.sendmail("kumargaurav6299@gmail.com", to, content)
    server.close()


def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%dhour,%02d minute, %02s seconds" % (hh, mm, ss)


if __name__ == "__main__":

    wish()
    while True:
        query = command().lower()

        #   Logic for executing the different task according to the given query
        # We are performing mulltiple task for different operations
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        # Everything about Jarvis

        elif 'hello' in query:
            print("Hello Sir")
            speak(" Hello Sir")


        elif 'how are you' in query:
            # print("I am fine Sir")
            speak("I am fine Sir, i am doing my work full of energy")
            speak("What about you sir")

        elif 'i am good' in query:
            speak("Thank you sir. And today weather is good. So please wake up and go to morning walk.")

        elif 'ok jarvis' in query:
            speak('ok sir')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir,the time is {strTime}")

        # Here we are going to Open many social media.

        elif 'open youtube' in query:
            speak("I am opening the youtube page for you")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("I am opening the google page for you")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("I am opening the stackoverflow page for you")
            webbrowser.open("stackoverflow.com")

        elif 'open hackerrank' in query:
            speak("I am opening the hackerrank page for you")
            webbrowser.open("hackerrank.com")


        elif 'open my website' in query:
            speak("I am opening your website")
            webbrowser.open("https://gaurav6299.github.io/Banner/")

        elif 'open facebook' in query:
            speak("I am opening the facebook for you")
            webbrowser.open("facebook.com")


        elif 'open flipkart' in query:
            speak("I am opening the flipkart for you")
            webbrowser.open("flipkart.com")

        elif 'open gmail' in query:
            speak("I am opening the gmail for you")
            webbrowser.open("gmail.com")

        elif 'open linkedin' in query:
            speak("I  am opening the linkedin for you")
            webbrowser.open("https://www.linkedin.com/in/kumar-gaurav-bb976b1a5")

        elif 'open instagram' in query:
            speak("I  am opening the instagram for you")
            webbrowser.open("instagram.com")


        elif 'open github' in query:
            speak("I am  opening the github for you")
            webbrowser.open("https:\\www.github.com")

        elif 'open twitter' in query:
            speak("I am opening the twitter for you")
            webbrowser.open("twitter.com")

        elif 'my location' in query:
            path = "https://goo.gl/maps/m1RqTEByW9h4Eraf8"
            webbrowser.open(path)



        # Here we are  gonna asking  from jarvis relationship

        elif 'who is your boyfriend' in query:
            print("my boyfriend is, salmaan")
            speak("my boyfriend is, salmaan")

        elif 'marry' in query or 'will you marry' in query:
            speak(" No")
            speak("I am sorry...The person you are trying to connect is currently unavailable, please try again later")


        elif 'who is my girlfriend' in query:
            print("your girlfriend is payal")
            speak("your girlfriend is payal")

        elif 'what is your name' in query:
            print("my name is, jarvis")
            speak("my name is, jarvis")

        elif 'what is your favourite colour' in query:
            speak('my favourite color is, yellow')

        elif 'what is my favourite colour' in query:
            speak('Your favourite color is, Blue')

        elif 'what is my date of birth' in query:
            print('Your date of birth is 26th march 2000. and you born in muzaffarpur in the state of bihar.')
            speak('Your date of birth is 26th march 2000. and you born in muzaffarpur in the state of bihar.')

        elif 'who i am' in query:
            speak(
                "You are kumar gaurav, and now you are pursuing b.tech in comuter science engineering from nalanda institute of technology, bhubaneswar.")

        elif 'who are you' in query:
            speak("I am not really a person, i am a i robot")
            speak(" I had prefer to think myself as your friend")

        elif 'favourite actress' in query:
            speak("there are so many talented actress in the world")
            speak("but my favourite actress is kajol")

        elif 'god exist' in query:
            speak("my boss gaurav, who created me he is exist")
            speak("that means god exist")


        elif 'favourite food' in query:
            speak("i like a lot of different foods")
            speak("i can help you find recipes or restaurents")

        elif 'you doing' in query:
            speak("Waiting for your command")


        elif 'd drive' in query:
            print('In open....')
            path = 'D:\\'
            speak('i am opening d drive')
            os.startfile(path)
            print('ok done')

        elif 'c drive' in query:
            print('In open...')
            path = 'C:\\'
            speak('i am opening c drive')
            os.startfile(path)
            print('ok done')

        elif 'e drive' in query:
            print('In open....')
            path = 'E:\\'
            speak("i am opening e drive")
            os.startfile(path)
            print('ok done')





        # here we are open differnt media player

        elif 'hit the music' in query:
            music_dir = 'E:\\FROM VIKASH PHONE\\music'
            songs = os.listdir(music_dir)
            speak("I am playing the music for you")
            print(songs)
            x = random.choice(songs)
            os.startfile(os.path.join(music_dir, x))


        elif 'open visual studio' in query:
            speak("I am opening the visual studio for you")
            path = "C:\\Users\\Kumar Gaurav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'open command' in query:
            speak("I opening the command for you")
            os.startfile("cmd")

        elif 'send email to gaurav' in query:
            try:
                speak("what should i say")
                content = command()
                to = "kumargaurav6299@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry gaurav bhai,I am not able to send your email")

        elif 'play the video' in query:
            speak("I am opening the video for you")
            path = "https://www.youtube.com/watch?v=IhaS1yZKuZU&t=9s"
            webbrowser.open(path)

        elif 'open my photo' in query:
            speak("I am showing your photo")
            path = "E:\\FROM VIKASH PHONE\\exotica 2k20\\IMG_20200202_151132.jpg"
            os.startfile(path)

        elif 'open calculator' in query:
            speak("I am opening the calculator in your pc")
            os.startfile("calc")

        elif 'open notepad' in query:
            speak("I am opening the notepad for you")
            os.startfile('notepad')

        # elif 'open calendar' in query:
        #     os.startfile("cale")

        elif 'open yahoo' in query:
            speak(' I am opening the yahoo for you')
            webbrowser.open("yahoo.com")


        elif 'screenshot' in query:
            speak('ok,sir let me take a snapshot')
            speak('ok done')
            speak('check your desktop,i have saved there')
            pic = pyautogui.screenshot()
            pic.save('C:/Users/Kumar Gaurav/OneDrive/Pictures/Screenshots.png')

        elif 'open skype' in query:
            webbrowser.open('skype.com')


        # charge

        elif 'charge' in query:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = int(battery.percent)
            time_left = secs2hours(battery.secsleft)
            print(percent)
            speak(percent)

            if percent < 40:
                speak("sir,  your battery is about to die,  please connect charger i can survive only" + time_left)
            if percent > 40:
                speak("dont't worry sir, charger is connected")

            else:
                speak("sir, no need to connect the charger because i can survive" + time_left)

        # Here we setting the brightness of the screen

        elif 'brightness' in query:
            if 'decrease' in query:
                print("ok listen....")
                dec = wmi.WMI(namespace='wmi')
                methods = dec.WmiMonitorBrightnessMethods()[0]
                speak("I am decreasing your laptop brightness sir ")
                methods.WmiSetBrightness(30, 0)

            elif 'increase' in query:
                print('ok listen....')
                ins = wmi.WMI(namespace='wmi')
                methods = ins.WmiMonitorBrightnessMethods()[0]
                speak("I am increasing your laptop brightness sir")
                methods.WmiSetBrightness(100, 0)


        # comparision between the different site

        elif 'better than google' in query:
            speak('No sir, google is great as compair to me, i am just a virtual assistance')

        elif 'better than alexa' in query:
            speak('No sir, alexa is a great assistance, so i like alexa')

        elif 'better than siri' in query:
            speak('No sir, siri is a great assistance, So i like siri')

        # open the english dictionary  and translate the word

        elif 'meaning' in query:
            dict = PyDictionary()
            speak(" Which word  you want to say")
            command()
            meaning = dict.meaning('spectacular')
            print(meaning)
            speak(f"the meaning of this word is {meaning}")


        #    open differnt cartoon

        elif 'open cartoon' in query:
            speak("I am opening cartoon for you")
            path = "https://www.youtube.com/watch?v=3sDB464E11A"
            webbrowser.open(path)

        # Show the  whole windows app

        elif 'open winword' in query:
            speak("I am opening word for you")
            os.startfile("winword.exe")


        elif 'open powerpoint' in query:
            speak(" I am opening powerpoint for you")
            os.startfile("powerpnt.exe")


        elif 'open excel' in query:
            speak(" I am opening excel for you")
            os.startfile("excel.exe")

        elif 'open my project' in query:
            webbrowser.open("http://localhost/project2/wordpress/")

        # lock screen opeartion

        elif 'lock my' in query:
            speak('ok, sir')
            ctypes.windll.user32.LockWorkStation()

        elif 'goodbye' in query:
            speak(' goodbye Sir, have a good day')
            sys.exit()

        elif 'shut down my computer' in query:
            speak("shutting down")
            os.system('shutdown -s')






