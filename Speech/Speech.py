import speech_recognition as sr
import pocketsphinx
import pyaudio
import pyttsx3
import time
import sys
from . import Router
sys.path.append('../CommandFunctionality')
import CommandFunctionality.wiki_handler as wh
import CommandFunctionality.request_handler as rh
import asyncio
class Speech:

    def __init__(self , parent ):
        self.router = Router.Router(self)
        self.request_handler = rh.RequestHandler(self)
        self.wiki_handler = wh.WikiHandler(self)
        self.parent = parent
        
        
    def say(self,text):
        engine = pyttsx3.init() 
        engine.say(text)
        engine.runAndWait()

    async def voice_input(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                a=r.listen(source,timeout=3)
                return  r.recognize_google(a)
            except:
               self.parent.speech.say("don't")
                

    async def gather_voice_init(self):
        data = await self.voice_input()
        if data == "Nova":
            self.say("Yes ,I am listening")
            await self.gather_voice_input_and_route()

    def silent_mode_temp(self):
        time.sleep(40)

    def silent_mode_until_turned_on(self):
        while True:
            data = self.voice_input()
            if data == "Nova turn on":
                break

    async def gather_voice_input_and_route(self):
        data = await self.voice_input()
        if data == None:
            self.say("Sorry Didn't quite get that!")
        else:
            self.router.route_priority_one(data)
    