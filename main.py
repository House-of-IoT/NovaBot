
from Speech.Speech import Speech
import socket



class Main:
    def __init__(self):
        self.speech = Speech()
        self.count = 0
        self.running = True

    def start(self):
        self.speech.say("You are not connected to the local server! Just a note.")
        self.speech.say("I am now listening for commands.")
        while self.running == True:
       
            self.speech.gather_voice_init()
    

if __name__ == "__main__":
    main = Main()
    main.speech.request_handler.say_geek_joke()
        
        