import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recogniser = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "API KEY of newsapi"

def speak(text):
    engine.say(text)
    engine.runAndWait()

# GOOGLE TEXT TO SPEECH (PAID)
# def speak(text):
#   tts = gTTS(text)
#   tts.save('temp.mp3')

#   # Initialize pygame mixer
#   pygame.mixer.init()

#   # Load the mp3 file
#   pygame.mixer.music.load("temp.mp3")  # Replace with your MP3 file path

#   # Play the mp3 file
#   pygame.mixer.music.play()
  
#   # keep the program running until the music stops playing
#   while pygame.mixer.music.get_busy():
#       pygame.time.Clock().tick(10)
#   pygame.mixer.music.unload()
#   os.remove("temp.mp3")

def aiprocess(command):
    client = OpenAI(
    api_key="API KEY of open ai"
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like alexa and google cloud. Give short responsses please."},
            {
                "role": "user",
                "content": command
            }
        ]
    )

    return completion.choices[0].message.content


def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open monkey type" in c.lower():
        webbrowser.open("https://monkeytype.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code==200:
            #parse the JSON response
            data = r.json()

            #extract the articles
            articles = data.get('articles', [])

            #print the headlines
            for article in articles:
                speak(article['title'])

    else:
        #let openai handle the request
        output = aiprocess(c)
        speak(output)



if __name__ == "__main__":
    speak("Initialising JARVIS...")
    while True:
        #listen for the wake word "JARVIS"
        #obtain audio from microphone
        r = sr.Recognizer()
        
        #recognise speech using google
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source,timeout=3,phrase_time_limit=3)

            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("yes")

                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)


        except Exception as e:
            print("Error; {0}".format(e))