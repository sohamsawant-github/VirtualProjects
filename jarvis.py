import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition as sr
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("Initializing jarvis")
speak("Initializing jarvis")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning sir!")

    elif 12 <= hour < 17:
        speak(f"Good Afternoon sir!")

    else:
        speak(f"Good Evening sir!")

    speak("I am Jarvis, Your personal desktop assistant. Please tell me how may i help you!")

def takeCommand():
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
        print("Unable to recognize your voice sir")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('forexample@gmail.com', 'your password')
    server.sendmail('forexample6@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open unacademy' in query:
            webbrowser.open("www.unacademy.com")

        elif 'open github' in query:
            webbrowser.open("www.github.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to soham' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "forexample@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif "good evening" in query:
            speak("Good evening sir")

        elif "good morning" in query:
            speak("Good morning sir")

        elif "good afternoon" in query:
            speak("Good afternoon sir")

        elif "shutdown" in query:
            speak("Hold on a second sir, Your system is on it's way to shutdown.")
            os.system("shutdown /s /t 5")

        elif "restart" in query:
            speak("Hold on a second sir, Your system is on it's way to restart.")
            os.system("shutdown /r /t 5")

        elif "ok bye" or "thanks bye" or "thank you" in query:
            speak("thanks for using me sir, have a nice day")
            print("thanks for using me sir, have a nice day")
            sys.exit()

      
        
        
        '''END OF JARVIS PROGRAM'''