from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np

ancho = 320
alto = 240

camera = PiCamera()
camera.resolution = (ancho, alto)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(ancho, alto))
time.sleep(0.1)





def ImagenPiCamaraBGR():
    camera.capture(rawCapture, format="bgr")
    MemoriaImagen = rawCapture.array
    return MemoriaImagen

def rostroVacio():
    rostro = np.ones((96, 96 ,3), np.uint8) 
    
time.sleep(0.1)