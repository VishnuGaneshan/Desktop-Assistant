import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init() #sapi5
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

MASTER="Vishnu"
print("Initializing Jarvis...")

#  To speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# To wish me with respect to time
def wishMe():
    wish=""
    hr = datetime.datetime.now().hour
    if(hr>=6 and hr<12):
        wish="Morning"
    elif(hr>=12 and hr<20):
        wish="Afternoon"
    elif(hr>=20 and hr<24):
        wish="Night"
    else:
        speak("sir, it is good to go and sleep, because it's a mid night")
        return None
    speak("Good "+wish+", "+MASTER)

# To listen to you and return what you said in text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}")
        return query
    
    except Exception as e:
        print("listening exception occured")
        #speak("sorry, can you say again please")
        return takecommand()

# chrome browser path setting 
chrome_path='c:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
   
# Logic starts here
def answer(query):
    # To wikipedia search
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query.replace("wikipedia","")
        query.replace("jarvis","")
        result = wikipedia.summary(query, sentences=2)
        print(result)
        speak(result)

    # To open youtube
    elif 'open youtube' in query:
        speak("opening youtube")
        url="youtube.com"
        try:
            webbrowser.get(chrome_path).open(url)
        except:
            return None

    # To search in youtube 
    # with passing parameter after asking
    elif 'search in youtube' in query:
        speak('what you want to search in youtube')
        query = takecommand()
        if query == "nothing":
            speak('okay sir')
        else:
            result=""
            query = query.split()
            for each in query:
                result +="+"+each
            url ="https://www.youtube.com/results?search_query=" + result
            webbrowser.get(chrome_path).open(url)

    # To open Whatsapp
    elif 'open whatsapp' in query:
        speak("opening whatsapp")
        url = "web.whatsapp.com"
        webbrowser.get(chrome_path).open(url)

    # To open Visual studio code
    elif 'open code' in query:
        codepath="C:\\Users\\Vishnu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

    # To search in google as same as like
    # for youtube search above
    elif 'search in google' in query:
        speak('what you want to search in google')
        query = takecommand()
        if query == "nothing":
            speak('okay sir')
        else:
            speak('searching '+query+' in google')
            result=""
            query = query.split()
            for each in query:
                result +="+"+each
            url ="https://www.google.com/search?q=" + result
            webbrowser.get(chrome_path).open(url)

    # To speak time
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    # To speak a list of what it can to
    elif 'what you can do' in query:
        list = ['search in wikipedia', 'search ,and open youtube'
        ,'open whatsapp','open visual studio code','search in google']
        for each in list:
            speak('i can '+each)
        speak('and i am thankful to vishnu for creating me to do this all things')
    
    elif 'open my project file' in query:
        codepath="C:\\Users\\Vishnu\\Desktop\\My Project\\Final_FaceMaskDetector.py"
        os.startfile(codepath)

    elif 'copy paste' in query:
        codepath="COPY&PASTE.py"
        os.startfile(codepath)
        speak('enter text here to paste there')

    elif 'go away' in query or 'sleep' in query:
        speak('thank you sir')
        return 'break'
        #try to break the while loop
    
    elif 'please stop' in query:
        speak('ok sir')
        input('enter something to start : ')
        speak('I am back')
    
    elif query =='jarvis':
        speak('yes sir !')
        query = takecommand().lower()
        answer(query)

    else:
        print('i cant do that')
        speak('sorry i cant do that')

wishMe()
#speak("Hi sir i am back")
while True:
    # To take query
    query = takecommand().lower()
    # query = query.lower()
    if 'jarvis' in query:
        bkpt=answer(query)
        if bkpt =='break':
            break
