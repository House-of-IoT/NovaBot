import speech_recognition as sr
import pocketsphinx
import pyaudio
from Router import Router 
import pyttsx3


class Speech:

    def __init__(self):
        self.router = Router(self,functionality)
        self.wiki_handler = functionality.wiki_handler.WikiHandler()
        
    def say(self,text):
        engine = pyttsx3.init() 
        engine.say(text)
        engine.runAndWait()

    def voice_input(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                a= r.listen(source,timeout=2,phrase_time_limit=2)
                return r.recognize_google(a)
            except:
                pass
    def gather_voice_input_then_route():
        data = self.voice_input()
        if data == None:
            self.say("Sorry Didn't quite get that!")
        else:
            self.router.route_priority_one(data)
