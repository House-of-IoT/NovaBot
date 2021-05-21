import socket
import threading
import asyncio
import websockets

class SocketHandler:
    def __init__(self ,parent):
        self.connected = False
        self.parent = parent
        self.connection = None
        
    async def listen(self ):
            try:
                websocket = await websockets.connect('ws://localhost:50223'  ,  ping_interval= None  , max_size = 20000000)
                while True: 
                    if self.connected == True:
                            if self.connection == None:
                                self.connection = websocket
                            message = await websocket.recv() 
                            print(message)
                            await self.route(message ,websocket)
                            await asyncio.sleep(2)                         
                    else:                           
                            message = await websocket.recv()
                            await websocket.send("will")
                            await websocket.send("bot")
                            response = await websocket.recv()
                            self.check_response(response)
            except Exception as e:
                print(e)

    def check_response(self,response ):
        if response == "connected!!":
            self.connected = True
            self.parent.speech.say("you are now connected to the remote server")
        else:
            self.parent.speech.say("Issue connecting to the remote server")
        
    async def route(self , command , websocket):
        print(command)
        if command == "say" or command == "device_data":
            data = await websocket.recv()
            self.parent.speech.say(data)
        elif command == "stream":
            self.parent.enabled = False
            self.parent.streaming = True
            self.parent.alarm = False
        elif command == "disable":
            self.parent.enabled = False
            print("disabled")
        elif command == "enable":
            self.parent.enabled = True
            self.parent.alarm = False
            self.parent.streaming = False
        elif command == "alarm":
            self.parent.enabled = False
            self.parent.streaming = False
            self.parent.alarm = True
        