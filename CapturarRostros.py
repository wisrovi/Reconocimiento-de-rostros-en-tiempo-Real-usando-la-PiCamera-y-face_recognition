from funcionesArchivos import *



rutaImagen = "pictures_of_people_i_know/"

import cv2
face_classifier = cv2.CascadeClassifier('detectors/haarcascade_frontalface_alt2.xml')

from piCamaraFunciones import *



def ObtenerRostroImagen(imagen):    
    ImagenTonosGrises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    CoordenadaRostro = face_classifier.detectMultiScale(ImagenTonosGrises, 1.2, 2)

    rostro = rostroVacio()
    HayRostros = False
    for (x,y,w,h) in CoordenadaRostro:
        rostro = MemoriaImagen[y:y+h,x:x+w]
        HayRostros = True
    return rostro, HayRostros
        
        
if ExisteArchivo(camaraOcupada)==False:
    crearArchivo(camaraOcupada)
    
nombreImagen = input(  "Digite su nombre sin espacios: ")

MemoriaImagen = ImagenPiCamaraBGR()
rostro, HayRostros = ObtenerRostroImagen(MemoriaImagen)

if HayRostros == True:
    cv2.imwrite(rutaImagen + nombreImagen + ".jpeg",rostro)
    print("rostro encontrado")
    
borrarArchivo(camaraOcupada)
if ExisteArchivo(camaraOcupada)==True:
    borrarArchivo(camaraOcupada)