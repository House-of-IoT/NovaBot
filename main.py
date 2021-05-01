import CommandFunctionality.wiki_handler
from Speech.Speech import Speech
import socket



class Main:
    def __init__(self):
        self.speech = Speech(CommandFunctionality.wiki_handler)
        self.count = 0
        self.running = True
        self.connected = False
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def connect_to_master_pi(self):
        try:
            self.client.connect(('127.0.0.1',50222))
        except:
            self.speech.say("Can't connect to server , please try again")

    def start(self):
        self.speech.say("You are not connected to the local server! Just a note.")
        self.speech.say("I am now listening for commands.")
        while self.running == True:
       
            self.speech.gather_voice_init()
    

if __name__ == "__main__":
    main = Main()
    main.start()
        
        