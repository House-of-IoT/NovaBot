import socket
import threading
import websockets
class SocketHandler:
    def __init__(self , parent):
        self.connected = False
        self.server_connection = None
        self.parent = parent


    async def listen(self):
        
            try:
                async with websockets.connect('ws://localhost:50223') as websocket:
                    while True:
                        
                        message = await websocket.recv()
                        await websocket.send("got")
                        if message == "disable":
                            self.parent.enabled = False
                        elif message == "say":
                            
                            self.parent.speech.say("got")
                        elif message == "stream_video":
                            pass
                        elif message == "stream_audio":
                            pass
                        elif message == "alarm":
                            pass
                        elif message == "performance":
                            pass
            except:
                pass
            
