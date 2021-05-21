import io
import time
import picamera
import asyncio

class CameraHandler:
    def __init__(self, parent):
        self.parent = parent
        self.setup_was_successful = True
        try:
            self.camera = picamera.PiCamera(framerate = 30)
            self.camera.vflip = True
            self.camera.resolution = (1024, 768)
            self.camera.start_preview()
            time.sleep(2)
            self.camera.stop_preview()
            self.stream = io.BytesIO()
        except:
            self.setup_was_successful = False
            
    async def stream_data(self , connection):

            for i in self.camera.capture_continuous(self.stream, 'jpeg' , use_video_port =True):
                self.stream.seek(0)
                await connection.send(self.stream.read())
                
                self.stream.truncate()
                await asyncio.sleep(0.5)
 


