import pyttsx3
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
from AppOpener import open

engine = pyttsx3.init("sapi5") #Windows default Voices Present
voices = engine.getProperty("voices")
engine.setProperty("voive",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def timenow():
    current_time = time.strftime("%H")
    if int(current_time)>=0 and int(current_time)<12:
        speak("Good Morning")
    elif int(current_time)>=12 and int(current_time)<24:
        speak("Good Evening")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ........")
        r.pause_threshold = 1
        r.energy_threshold = 10
        audio = r.listen(source)

    try:
        print("Recognizing .....")
        query = r.recognize_google(audio , language = "en-in")
        print("User Said :- " , query)
    except Exception as e:
        print("Please Say Again")
        return "None"
    return query

if __name__ == "__main__":

    timenow()
    speak("Sir , This is David, your personal assistant . What task would you like me to perform?")
    while True:
        query = takecommand().lower()

        if "what can you do" in query:
            speak("I may serach things on wikipedia , may tell you current time , remind you after few minutes , can perform several tasks like opening any application , May I know how may i help you ?")

        # Performing Task Using Websites
        elif "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia" , "") # This is done otherwise search about xyz on *wikipedia* will be searched on wikepedia , so we remove the word wikipedia and get the result search about xyz
            results = wikipedia.summary(query , sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            urL='http://www.youtube.com'
            webbrowser.open(urL)
            speak("Opening Youtube")

        elif "open spotify" in query:
            urL='https://open.spotify.com/'
            webbrowser.open(urL)
            speak("Opening Spotify")
        
        #Basic Task Regarding Time
        elif "current time" in query:
            speak("the current time is")
            speak(datetime.datetime.now().strftime("%H:%M:%S"))

        elif "reminder for 1" in query:
            time.sleep(60)
            speak("Sir , this is the 1 minute reminder")

        elif "reminder for 5" in query:
            time.sleep(300)
            speak("Sir , this is the 5 minute reminder")

        elif "reminder for 10" in query:
            time.sleep(600)
            speak("Sir , this is the 10 minute reminder")
        
        #Appreciate or Not Impressed
        elif "nice work david" in query:
            speak("Thanks a lot sir")

        elif "not impressed" in query:
            speak("Sorry sir , will improve in future")
            
        #To Stop the program:- 
        elif "stop" in query:
            speak("Thanks For Calling me , See you later")
            break
        elif "quit" in query:
            speak("Thanks For Calling me , See you later")
            break

        #To Open Applications
        elif "open" in query:
            query = query.replace("open" , "")
            speak(f"Opening {query}")
            open(f"{query}")

