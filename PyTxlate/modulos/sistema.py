import os
import time
from art import *

def cls(): # Limpiar consola
    os.system('cls')

def separador():  # separador con "="
    print("=" * 70) 

def creditos():
    lucy = "LUCYFER"  # Variable con mi nombre to' bonito...
    print(f"{lucy:=^71}")  #... y lo centramos usando "=" de relleno
    print()

def pantalla():  # Creamos funcion para limpiar y mostrar informacion en consola
    cls()
    tprint("           PyTxLate")
    creditos()

def cambiar_nombre():
    ruta_traducido = "archivo_unido.txt"
    nombre_usuario = input("Ingrese el nombre de su archivo\n> ")
    ruta_nuevo_nombre = os.path.join(ruta_fin_traducido(), nombre_usuario + ".txt")
    os.rename(ruta_traducido, ruta_nuevo_nombre)
    print(f"El archivo {nombre_usuario}.txt se ha creado correctamente")
    time.sleep(5)

def obt_ruta_inicial():
    ruta_archivo = input("Ingresa la ruta del archivo a leer:\n > ")
    ruta_archivo = ruta_archivo.replace('"', '')  # Eliminar comillas
    return ruta_archivo

def ruta_fin_traducido():
    descargas_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    carpeta_traducciones = os.path.join(descargas_path, 'traducciones') 
    if not os.path.exists(carpeta_traducciones):
        os.makedirs(carpeta_traducciones)
    return carpeta_traducciones