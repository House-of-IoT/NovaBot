import socket
import threading
import asyncio
import websockets

class SocketHandler:
    def __init__(self ,parent):
        self.connected = False
        self.parent = parent

    async def listen(self ):
            websocket = await websockets.connect('ws://localhost:50223'  ,  ping_interval= None )

            while True: #Run this forever
                try:    
                    if self.connected == True:
                            message = await websocket.recv() #recv
                            await asyncio.sleep(3)
                          
                    else:
                            
                            message = await websocket.recv()
                            await websocket.send("bot")
                            await websocket.send("will")
                            message = await websocket.recv()
                            self.connected = True
                except Exception as e:
                    print(e)
             

        
