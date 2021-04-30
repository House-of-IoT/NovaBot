import speech_recognition as sr
import pocketsphinx
import pyaudio
import pyttsx3


class Speech:


    def say(self,text):
        engine = pyttsx3.init() 
        engine.say(text)
        engine.runAndWait()

    def voice_input(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                a= r.listen(source,timeout=2,phrase_time_limit=1.7)
                return r.recognize_google(a)
            except:
                pass
print(Speech().voice_input())
    