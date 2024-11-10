# DeskTop-AI-Assistant

A voice-controlled AI assistant for Windows, designed to perform a variety of tasks like opening applications, answering questions, chatting with the user, and more, using voice commands.

Features
Voice Command Recognition: Uses a microphone to listen for commands and provide responses.

Text-to-Speech (TTS): The assistant speaks responses aloud using pyttsx3.

AI Chat Integration: Powered by OpenAI's GPT-3 to answer questions and engage in conversations.

Application Control: Opens websites and system applications such as Notepad, Calculator, Spotify, and more.

Time Reporting: Announces the current time when asked.

Music Control: Can play music files stored on the system.

Prerequisites
Before you start, you will need to have the following installed:

Python 3.x (Preferably Python 3.7+)
Required Python Libraries:
sounddevice
numpy
scipy
speech_recognition
pyttsx3
openai
webbrowser
subprocess
datetime
You can install the required libraries using pip:

pip install sounddevice numpy scipy SpeechRecognition pyttsx3 openai
Additionally, you will need to set up OpenAI API keys.

Setting Up OpenAI API

Create an account on OpenAI.

Go to API Keys and generate an API key.

Save the API key in a file named config.py inside the project directory with the following structure:

python
Copy code
apikey = 'your-openai-api-key-here'
Usage
Clone the repository or download the project files to your local machine.

Commands you can use:

Open applications (e.g., "Open Google", "Open Notepad", "Open YouTube")

Ask for the time ("What is the time?")
Play music ("Open music")
AI Chat ("Using artificial intelligence, tell me a joke")
Reset chat history ("Reset chat")
Exit the assistant ("Jarvis Quit")


Ensure your microphone is set up correctly and is recognized by your system.
You can adjust the sensitivity by modifying the duration of the audio recording in takeCommand() function if necessary.
Missing Libraries:

If any libraries are missing, install them via pip (e.g., pip install pyttsx3).


Make sure your API key is correctly set in config.py.
If you encounter errors with OpenAI, make sure the API quota is available.
License
This project is licensed under the MIT License - see the LICENSE file for details.

How to Customize
Music Path: Modify the path to your music files in the if "open music" in query section.
Add More Applications: Expand the applications dictionary in the script to include more commands and links to open additional apps or websites.
AI Prompt Handling: Customize the AI's behavior and responses by adjusting the ai() and chat() functions to better suit your needs.
