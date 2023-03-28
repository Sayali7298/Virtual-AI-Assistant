import pyttsx3
import pywin32_system32
import datetime
import speech_recognition as sr
import wikipedia
#import anigravity
import webbrowser as wb
import os
import random
import pyautogui
#import browser as b
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

def wishme():
    print("Welcome back maam!!")
    speak("Welcome back maam!!")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning maam!!")
        print("Good Morning maam!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon maam!!")
        print("Good Afternoon maam!!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening maam!!")
        print("Good Evening maam!!")
    else:
        speak("Good Night maam, See You Tommorrow")

    speak("Jarvis at your service maam, please tell me how may I help you.")
    print("Jarvis at your service maam, please tell me how may I help you.")

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\AI Assistant\Images")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I'm JARVIS created by Miss Sayali and I'm a desktop voice assistant.")
            print("I'm JARVIS created by Miss Sayali and I'm a desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine maam, What about you?")
            print("I'm fine maam, What about you?")

        elif "fine" in query:
            speak("Glad to hear that maam!!")
            print("Glad to hear that maam!!")

        elif "good" in query:
            speak("Glad to hear that maam!!")
            print("Glad to hear that maam!!")

        elif "wikipedia" in query:
            try:
                speak("Ok wait maam, I'm searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page maam, please ask something else")
        
        elif "open youtube" in query:
            wb.open("youtube.com") 

        elif "open google" in query:
            wb.open("google.com") 
   
        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        # elif "play music" in query:
        #     song_dir = "C:\\Users\\KISHAN\\Music"
        #     songs = os.listdir(song_dir)
        #     print(songs)
        #     x = len(songs)
        #     y = random.randint(0,x)
        #     os.startfile(os.path.join(song_dir, songs[y]))

        elif "open chrome" in query:
          #  chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\Chrome.exe"
            os.startfile(chromePath)

        elif "search on chrome" in query:
            try:
                speak("What should I search?")
                print("What should I search?")
                chromePath = "C:\Program Files\Google\Chrome\Application\Chrome.exe"
                search = takecommand().lower()
                
                wb.open_new_tab(search)
  
            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")
            
        
        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")


        elif "offline" in query:
            quit()


