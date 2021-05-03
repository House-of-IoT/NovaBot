
from Speech.Speech import Speech
from CommandFunctionality.socket_handler import SocketHandler
import socket

class Main:
    def __init__(self):
        self.speech = Speech(self)
        self.count = 0
        self.running = True
        self.enabled = True
        self.socket_handler =  SocketHandler(self)

    def start(self:int) :
        self.speech.say("Hello")
        self.socket_handler.connect_to_master_pi()
        while self.running == True:
            if self.enabled == True:
                self.speech.gather_voice_init()


    
if __name__ == "__main__":  
    main = Main()
    main.start()
        
        