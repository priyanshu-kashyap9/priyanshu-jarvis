import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

#pip install pocketsphinx


reconizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif c.lower().startswith("play"):
        song =c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    # elif "news " in c.lower():
    #     r = requests.get("apilinkprovide ") 
    #     if r.status_code ==200:
    # #prase the json  response
    #         data =r.json()

    # #extract the articles
    #     articles = data.get('articles',[])

    # # print the headlines
    #     for article in articles:
    #         speak(article['title'])     

    # else 
    #let openAi handel the request





if __name__=="__main__":
    speak(" Initializing  own jarvis ...")
    while True:
        #listen for the wake words jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        # reconize speech using google
        print("reconizing ...")
        try:
            with sr.Microphone() as source:
                print("listening")
                audio = r.listen(source , timeout=2,phrase_time_limit=1)
                word = r.reconize_google(audio)
            if(word.lower() == "own jarvis"):
                speak("yaa")
            #listen for command 
            with sr.Microphone() as source:
                print("jarvis active ")
                audio = r.listen(source)
                command = r.reconize_google(audio)

                processCommand(command)
        except Exception as e:
            print("error ; {0}".format(e))
            