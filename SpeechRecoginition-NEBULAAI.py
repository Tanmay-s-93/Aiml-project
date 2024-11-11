import os
import pyjokes
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import smtplib

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change to 0 for male voice

# Function to speak the given audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to send an email
def send_email(to, content):
    EMAIL_ADDRESS = os.getenv('EMAIL_USER')  # Set your email in environment variables
    EMAIL_PASSWORD = os.getenv('EMAIL_PASS')  # Set your password in environment variables
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(f"Error: {str(e)}")
        speak("Sorry, I couldn't send the email due to an error.")

# Function to wish the user based on the time of day
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Nebula. Please tell me how may I help you.")

# Function to take voice commands from the user
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
        return query.lower()
    except Exception as e:
        print("Sorry, I didn't catch that. Could you repeat?")
        return "none"

# Main function to execute tasks based on user commands
def main():
    wish_me()
    while True:
        query = take_command()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace('wikipedia', '')
                results = wikipedia.summary(query, sentences=2, auto_suggest=False)
                speak('According to Wikipedia:')
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak('Sorry, I could not find any results on Wikipedia.')

        elif "shutdown" in query:
            speak("Are you sure you want to shut down the system?")
            confirmation = take_command()
            if "yes" in confirmation:
                os.system("shutdown /s /t 1")
                break

        elif "restart" in query:
            speak("Are you sure you want to restart the system?")
            confirmation = take_command()
            if "yes" in confirmation:
                os.system("shutdown /r /t 1")
                break

        elif "sleep" in query:
            speak("Are you sure you want to put the system to sleep?")
            confirmation = take_command()
            if "yes" in confirmation:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                break

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            print("Opening YouTube...")

        elif 'open google' in query:
            webbrowser.open("google.com")
            print("Opening Google...")

        elif 'play music' in query:
            music_dir = os.path.expanduser("~/Music")
            print("Opening Music")
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("No music files found.")

        elif 'time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")
            print(str_time)

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "yourfriend@gmail.com"  # Change to the recipient's email
                send_email(to, content)
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't send the email.")

        elif "joke" in query:
            joke = pyjokes.get_joke(language="en", category="neutral")
            print(joke)
            speak(joke)

        elif 'thank you' in query:
            speak("You're welcome! I'm here to help.")

        elif 'open new erp' in query:
            webbrowser.open("https://newerp.kluniversity.in/index.php")
            speak("Opening New ERP for you...")

        elif 'open bmp' in query:
            webbrowser.open("https://bmp-lms.klh.edu.in/login/index.php")
            speak("Opening BMP LMS for you...")

        elif 'open spotify' in query:
            webbrowser.open("https://open.spotify.com/")
            speak("Opening Spotify for you...")

        elif 'explain about yourself' in query:
                speak("Nebula Virtual Assistant is a AI based system written in python that uses natural language processing and voice recognition to automate your tasks via proper task description using voice commands. Nebula is an everyday assistant that listens to spoken commands, helping people locate restaurants nearby, sending email drafts at designated timestamps, searching the web and buying goods. With external libraries seamlessly incorporated for speech recognition, text to speech and task automation; Nebula provides an easy-to-use user interface concentrating on convenience and increasing productivity. This project exemplifies usage of AI techniques in developing responsive and interactive systems to address common needs.")
                print("Nebula Virtual Assistant is a AI based system written in python that uses natural language processing and voice recognition to automate your tasks via proper task description using voice commands. Nebula is an everyday assistant that listens to spoken commands, helping people locate restaurants nearby, sending email drafts at designated timestamps, searching the web and buying goods. With external libraries seamlessly incorporated for speech recognition, text to speech and task automation; Nebula provides an easy-to-use user interface concentrating on convenience and increasing productivity. This project exemplifies usage of AI techniques in developing responsive and interactive systems to address common needs.")

        elif 'quit' in query:
            speak("Thank you! Have a nice day.")
            print("Thank you! Have a nice day.")
        elif 'open facebook' in query:
                webbrowser.open("https://www.facebook.com/")
                speak("opening facebook for you")
        elif 'open gemini' in query:
                    webbrowser.open("https://gemini.google.com/app")
                    speak("Opening perplexity for you")
        elif 'open netflix' in query:
                        webbrowser.open("https://www.netflix.com/browse")
                        speak("Opening netflix")
        break

if __name__ == "__main__":
    main()
