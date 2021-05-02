import speech_recognition as sr
import pocketsphinx
import pyaudio
import pyttsx3
import sys
from . import Router
sys.path.append('../CommandFunctionality')
import CommandFunctionality.wiki_handler as wh
import CommandFunctionality.request_handler as rh

class Speech:

    def __init__(self ):
        self.router = Router.Router(self)
        self.request_handler = rh.RequestHandler(self)
        self.wiki_handler = wh.WikiHandler(self)
        
        
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

    def gather_voice_init(self):
        data = self.voice_input()
        if data == "Nova":
            self.say("Yes ,I am listening")
            self.gather_voice_input_and_route()

    def gather_voice_input_and_route(self):
        data = self.voice_input()
        if data == None:
            self.say("Sorry Didn't quite get that!")
        else:
            self.router.route_priority_one(data)
