
from Speech.Speech import Speech
from CommandFunctionality.socket_handler import SocketHandler
import websockets
import asyncio

class Main:
    def __init__(self):
        self.speech = Speech(self)
        self.count = 0
        self.running = True
        self.enabled = True 
        self.alarm = False
        self.streaming = False
        self.socket_handler =  SocketHandler(self)
        self.tasks = []

    async def start(self:int) :

            self.speech.say("Hello")
            while True:
                await asyncio.sleep(3)
                if self.enabled == True:
                    await self.speech.gather_voice_init()
                else:
                    if self.streaming == True:
                        pass #stream 
                    else:
                        pass #do nothing



    async def listen(self):
            
            t2 = loop.create_task(self.start())
            t1 = loop.create_task(self.socket_handler.listen())
            await asyncio.wait([t1,t2])


    
if __name__ == "__main__":  
  main = Main() 
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main.listen())



  
  

  

        