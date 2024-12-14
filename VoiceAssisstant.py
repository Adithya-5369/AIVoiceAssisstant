import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import smtplib
from requests import get
import wikipedia
from PyDictionary import PyDictionary as Diction
import keyboard
import sys

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Configurations (Update paths and email credentials here)
CONFIG = {
    "applications": {
        "vlc": "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe",
        "notepad": "C:\\WINDOWS\\system32\\notepad.exe",
        "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    },
    "email": {
        "address": "your_email@gmail.com",
        "password": "your_email_password"
    },
    "music_directory": "C:\\Users\\Public\\Music"  # Update this to your music folder
}

# Text-to-Speech Function
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Speech-to-Text Function
def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
        except Exception:
            speak("I couldn't understand. Please say that again.")
            return "none"
        return query.lower()

# Email Function
def sendEmail(to, content):
    try:
        email_config = CONFIG["email"]
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_config["address"], email_config["password"])
        server.sendmail(email_config["address"], to, content)
        server.close()
        speak("Email has been sent successfully.")
    except Exception as e:
        speak("Unable to send the email. Please check your credentials.")
        print(e)

# Open Applications
def openApplication(app_name):
    try:
        app_path = CONFIG["applications"].get(app_name.lower())
        if app_path:
            os.startfile(app_path)
            speak(f"{app_name} is opening.")
        else:
            speak(f"I couldn't find the path for {app_name}. Please check the configuration.")
    except Exception as e:
        speak(f"An error occurred while trying to open {app_name}.")
        print(e)

# Dictionary Functionality
def useDictionary():
    dictionary = Diction()
    speak("Dictionary is active. What would you like to know?")
    query = takeCommand()
    if 'meaning' in query:
        word = query.replace("meaning of", "").strip()
        meaning = dictionary.meaning(word)
        speak(f"The meaning of {word} is: {meaning}")
    elif 'synonym' in query:
        word = query.replace("synonym of", "").strip()
        synonyms = dictionary.synonym(word)
        speak(f"The synonyms of {word} are: {synonyms}")
    elif 'antonym' in query:
        word = query.replace("antonym of", "").strip()
        antonyms = dictionary.antonym(word)
        speak(f"The antonyms of {word} are: {antonyms}")
    else:
        speak("Sorry, I couldn't understand. Please ask for meaning, synonym, or antonym.")

# Core Functionality
def main():
    speak("Initializing Smart Assistant.")
    while True:
        query = takeCommand()

        if 'open' in query:
            app_name = query.replace("open", "").strip()
            openApplication(app_name)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("To whom should I send the email?")
                to_email = input("Enter recipient email: ")  # User input for email ID
                sendEmail(to_email, content)
            except Exception as e:
                speak("Something went wrong while sending the email.")
                print(e)

        elif 'search wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("search wikipedia for", "").strip()
            try:
                result = wikipedia.summary(query, sentences=2)
                speak(f"According to Wikipedia, {result}")
            except Exception as e:
                speak("I couldn't find anything on Wikipedia.")
                print(e)

        elif 'google search' in query:
            query = query.replace("google search for", "").strip()
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak("Here are the search results.")

        elif 'play music' in query:
            music_dir = CONFIG["music_directory"]
            try:
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                    speak("Playing music.")
                else:
                    speak("No music found in the directory.")
            except Exception as e:
                speak("An error occurred while trying to play music.")
                print(e)

        elif 'dictionary' in query:
            useDictionary()

        elif 'shutdown' in query:
            speak("Shutting down. Goodbye!")
            sys.exit()

        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}.")

        else:
            speak("I couldn't understand that. Can you please repeat?")

# Main Execution
if __name__ == "__main__":
    main()
