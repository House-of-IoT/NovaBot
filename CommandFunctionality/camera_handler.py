import io
import socket
import struct
import time
import picamera

class CameraHandler:
    def __init__(self):
        try:
            self.camera = picamera.PiCamera()
            self.camera.vflip = True
            self.camera.resolution = (300, 280)
            self.camera.start_preview()
            time.sleep(2)
        except:
            pass
            