from Speech.Speech import Speech
from CommandFunctionality.socket_handler import SocketHandler
from CommandFunctionality.camera_handler import CameraHandler
import asyncio

class Main:
    def __init__(self):
        self.speech = Speech(self)
        self.count = 0
        self.enabled = True 
        self.alarm = False
        self.streaming = False
        self.socket_handler =  SocketHandler(self)
        self.camera_handler = CameraHandler(self)

    async def start(self:int) :

            self.speech.say("Welcome Back")
            while True:
                await asyncio.sleep(3)

                if self.enabled == True:
                    await self.speech.gather_voice_init()
                else:
                    if self.streaming == True:
                        if self.camera_handler.setup_was_successful:
                            self.camera_handler.stream_data(self.socket_handler.connection)
                        else:
                            self.enabled = True
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



  
  

  

        