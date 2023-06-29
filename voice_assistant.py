import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process voice commands
def process_command(command):
    command = command.lower()

    if "hello" in command:
        speak("Hello there!")

    elif "how are you" in command:
        speak("I'm doing well, thank you!")

    elif "what is your name" in command:
        speak("My name is Voice Assistant")

    elif "goodbye" in command:
        speak("Goodbye!")

    else:
        speak("Sorry, I didn't understand that command.")

# Main loop
while True:
    try:
        # Capture audio from microphone
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        # Recognize speech
        command = recognizer.recognize_google(audio)
        print("You said:", command)

        # Process the command
        process_command(command)

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError:
        print("Sorry, I'm having trouble connecting to the speech recognition service.")
