import qrcode
import time
import sys

def generando_codigo():
    print ("este es un programa que te pide un enlace o texto y te genera un codigo QR en formato .PNG")
    time.sleep(3)

    codificar = input (f'COMENCEMOS!\nQue palabra o enlace quieres que te codifique en QR?')
    print ('Codificando...')
    time.sleep(3)
    img = qrcode.make(codificar)
    f = open(codificar+"_QR.png", 'wb')
    img.save(f)
    print(f'LISTO\nTienes la imagen correctamente creada con el nombre {codificar}_QR.png')
    time.sleep(2)
    preguntar_Opcion()

def preguntar_Opcion():
    opcion = input(f'Que Quieres hacer ahora? (H)acer otro codigo? / (S)alir del programa?')
    if opcion == 'h' or opcion == 'H':
        generando_codigo()
    else:
        time.sleep(0.4)
        print ("Hasta pronto!")
        sys.exit()

generando_codigo()
