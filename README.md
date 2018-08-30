# Reconocimiento-de-rostros-en-tiempo-Real-usando-la-PiCamera-y-face_recognition

Vamos a continuar donde lo dejamos en https://github.com/wisrovi/PiCamera-convertir-rostros-en-base-de-datos-codificada

# Ejecutando el programa

Para iniciar la aplicación se ejecuta  ReconocerPersonaRTC.py este archivo importara todas las librerias  necesarias que hemos visto en las dos fuentes anteriores.

Si la persona ya ha registrado su rostro y actuualizado los .csv de encoded de estas imagenes, el sistema en tiempo real imprimira el nombre de la persona en pantalla, en caso de que la persona no este regisrada impimira un mensaje de "Sin clasificar" se imprimirá en pantalla.

Adicionalmente si se desea incluir una nueva persona se debe ejecutar el archivo  CapturarRostros.py y seguido el archivo actualizarDatosRF.py, con esto cuando este en ejecución el  ReconocerPersonaRTC.py reconocera a la persona que este en frente de la camara.
