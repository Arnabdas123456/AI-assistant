import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#print(voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
        
    else:
        speak("Good Evening sir!")

    speak("I am Maria. please tell me how may I help you")
def talkcommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except  Exception as e:
         #print(e)
         print("Say that again please......")
         return "None"
    return query


if __name__ == '__main__':
    wish()
    while True:

        query = talkcommand().lower()

        #logic on executing task base on query
        if 'wikipedia' in query:
            speak('Searching wikipedia......')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play song' in query:
            music_dir = "C:\\Users\\LENOVO\\PycharmProjects\\AI\\audio"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is{strTime}")

        elif 'open my code' in query:
            codepath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)


