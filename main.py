import speech_recognition as sr
import webbrowser
import pyttsx3

# webbrowser.open("https://www.google.com")

reconizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
if __name__=="__main__":
    speak(" hello sir i am priyanshu")