# importing libraries
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme(datetime):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hey sir, jarvis here; please let me know how may i help you?")


def takecommand():
    # it takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:", query)
    except Exception as e:
        print(e)
        speak("say that again please......")
        return "None"
    return query


if __name__ == '__main__':
    # speak("Vinay is Good boy")
    wishme(datetime)
    while True:
        # if 1:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia.............please wait for a while")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open notepad' in query:
            npath = 'C:\\windows\\system32\\notepad.notepad.exe'
            os.startfile(npath)

        elif 'open command prompt' in query:
            os.system('start cmd')

        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")

        elif 'open calendar' in query:
            webbrowser.open("www.calendar.com")

        elif 'open code' in query:
            # change path according to your username
            codepath = "C:\\Users\\imvin\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codepath)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%h:%m:%S")
            speak(f"sir the time is{strTime}")

        elif 'stop' in query:
            speak("Thank you for using me. have good day")
            sys.exit()

        else:
            speak('unregistered command')
