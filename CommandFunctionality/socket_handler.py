import socket
import threading

class SocketHandler:
    def __init__(self , parent):
        self.connected = False
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.parent = parent

    def connect_to_master_pi(self):
        try:
            self.client.connect(('127.0.0.1',50222))
            return True
        except:
            self.speech.say("Can't connect to server , please try again")
            return False

    def listen():
        message = self.client.recv(100).decode("utf8")
        if message == "disable":
            self.parent.enabled = False
        elif message == "say":
            phrase = self.client.recv(100).decode("utf8")
            self.parent.speech.say(phrase)
        elif message == "stream_video":
            pass
        elif message == "stream_audio":
            pass
        elif message == "alarm":
            pass
        elif message == "performance":
            pass
        
    def start_listening_from_master():
        if self.connect_to_master_pi() == True:
            thread = threading.Thread(target= self.listen)
            thread.start()

