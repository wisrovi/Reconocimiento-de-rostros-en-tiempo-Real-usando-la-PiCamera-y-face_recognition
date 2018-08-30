from funciones import *

import picamera
import numpy as np
camera = picamera.PiCamera()
camera.resolution = (320, 240)
MemoriaImagen = np.empty((240, 320, 3), dtype=np.uint8)


print("Base de datos Actualizada")
ActualizarBaseDatos()

print("Base de datos de personas cargada.")

datos = datosPersonas()

while True:
    if ExisteArchivo(camaraOcupada)==False:
        if procesoCopiarBaseDatos()== True:
            print("--- Actualizando datos internos ---")
            datos = datosPersonas()           
        
        camera.capture(MemoriaImagen, format="rgb")

        ubicacionRostros = localizacionRostros(MemoriaImagen)
        cantidadRostros = conteoRostrosImagenCompleta(ubicacionRostros)
        
        if cantidadRostros == 0:
            print("Any person")
        rostrosCodificados = codificarRostrosImagenCompleta(MemoriaImagen, ubicacionRostros)

        for rostroUnitarioCodificado in rostrosCodificados:               
            nombrePersona = compararDatosVsImagenActual(datos, rostroUnitarioCodificado, 0.5)
            print("Reconozco a: %s" %(nombrePersona))
    else:
        print(".")
        pausarSegundos(1)
