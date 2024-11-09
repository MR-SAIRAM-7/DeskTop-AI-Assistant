import sounddevice as sd
import numpy as np
import os
import scipy.io.wavfile as wav
import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import datetime
import openai
from config import apikey

# Declare chatStr as global at the top level
chatStr = ""

def say(text):
    """Use text-to-speech to speak the given text."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def chat(query):
    """Chat with the AI assistant."""
    global chatStr  # Declare chatStr as global before modifying it
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Harry: {query}\n Jarvis: "
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatStr,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        reply = response["choices"][0]["text"]
        say(reply)
        chatStr += f"{reply}\n"
    except Exception as e:
        print(f"Error in AI chat: {e}")
        say("Sorry, I couldn't process your request.")
        reply = ""
    
    return reply

def ai(prompt):
    """Generate AI response for a given prompt and save it to a file."""
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        text += response["choices"][0]["text"]
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        
        # Save the response to a file
        safe_prompt = ''.join(prompt.split('intelligence')[1:]).strip()
        with open(f"Openai/{safe_prompt}.txt", "w") as f:
            f.write(text)
    except Exception as e:
        print(f"Error in AI prompt processing: {e}")
        say("Sorry, I couldn't process your request.")

def takeCommand():
    """Listen for a voice command and return the recognized text."""
    fs = 44100  # Sample rate
    seconds = 5  # Duration of recording
    print("Listening...")

    # Record audio with sounddevice
    audio_data = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()  # Wait until the recording is finished

    # Save the recorded audio to a temporary WAV file
    wav.write("temp.wav", fs, audio_data)

    # Use speech_recognition to process the WAV file
    r = sr.Recognizer()
    with sr.AudioFile("temp.wav") as source:
        audio = r.record(source)  # Read the entire audio file

    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I did not catch that.")
        query = ""
    except sr.RequestError:
        print("Network error.")
        query = ""

    # Clean up the temporary file
    if os.path.exists("temp.wav"):
        os.remove("temp.wav")
    
    return query.lower()

# Dictionary mapping voice commands to applications/URLs
applications = {
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "spotify": "https://open.spotify.com",
    "instagram": "https://instagram.com",
    "calculator": "calc",  # Opens Calculator
    "notepad": "notepad",  # Opens Notepad
    "paint": "mspaint",  # Opens Paint
    "file explorer": "explorer",  # Opens File Explorer
    "command prompt": "cmd",  # Opens Command Prompt
    "task manager": "taskmgr",  # Opens Task Manager
    "control panel": "control",  # Opens Control Panel
    "powershell": "powershell",
    "twitter": "https://x.com",  # Opens Twitter
}

# Introduction
say("Hi Sai, I'm Jarvis, Your AI Assistant")

# Main loop to continuously listen and process commands
while True:
    query = takeCommand()  # Get user command
    
    if query:
        # Loop through applications to find a match in the query
        for app, command in applications.items():
            if f"open {app}" in query:
                say(f"Opening {app.capitalize()}...")
                
                # Check if the command is a URL or a system application
                if "https://" in command or "http://" in command:
                    webbrowser.open(command)  # Open the URL in the browser
                else:
                    subprocess.run(command, shell=True)  # Execute the system command to open the application
                break  # Exit the loop after opening the application
        
        # Check if user requested to play music
        if "open music" in query:
            musicpath = "D:/music/chutti.mp3"  # Make sure the path is correct
            if os.path.exists(musicpath):
                os.system(f"start {musicpath}")  # Open the music file in the default music player
            else:
                say("Sorry, I could not find the music file.")

        # Provide the current time
        elif "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {strfTime}")
            
        # Handle AI prompt request
        elif "using artificial intelligence" in query:
            ai(prompt=query)

        # Exit the program
        elif "jarvis quit" in query:
            say("Goodbye, Sai. Jarvis is shutting down.")
            break

        # Reset the chat history
        elif "reset chat" in query:
            chatStr = ""

        # Chat with the assistant for general queries
        else:
            print("Chatting...")
            chat(query)
