
import socket
import websockets
import asyncio
class Server:
    def __init__(self):
        self.host = '127.0.0.1' #localhost for testing
        self.port = 50222
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = True
        self.connected = 0
        self.server.bind((self.host,self.port))
        self.server.listen()
        self.clients = {}
    
    def start_local_server(self):
        while self.running == True:
            client , addr = self.server.accept()
            self.connected += 1 
            name = client.recv(100).decode("utf8")
            self.clients[name] = client
            
    async def listen_to_remote_server(self,addr):
        try:
            async with websockets.connect(addr) as websocket:
                server_command = await websocket.recv()
        except:
            pass