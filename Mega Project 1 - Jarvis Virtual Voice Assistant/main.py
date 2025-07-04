import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "cbac8b4bcb9245dd94759d9836e79326"

def old_speak(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    # Initialize mixer and pygame
    pygame.init()
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")

    # Play the music
    pygame.mixer.music.play()

    # Keep the program running until music ends
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split("")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        # Check if request was successful
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            #Speak the headlines
            for article in articles:
                speak(article['title'])
    else:
        # Let openAI handle the request
        pass
        # it requires a paid version of openAI to integrate the AI 




if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:        
        # Listen for the wake word "Jarvis"
        r = sr.Recognizer()

        

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yes Sir")
                #Listen for the command
                with sr.Microphone() as source:
                    print("Jarvis Activated...")
                    audio = r.listen(source)
            command = r.recognize_google(audio)

            processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))