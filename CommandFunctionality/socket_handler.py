import socket
import threading

class SocketHandler:
    def __init__(self):
        self.connected = False
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_master_pi(self):
        try:
            self.client.connect(('127.0.0.1',50222))
            return True
        except:
            self.speech.say("Can't connect to server , please try again")
            return False
            
    def listen():
        message = self.client.recv(100).decode("utf8")
        
    def start_listening_from_master():
        if self.connect_to_master_pi() == True:
            thread = threading.Thread()

