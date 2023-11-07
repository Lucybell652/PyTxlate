import os
import pygame
from modulos.sistema import (
    pantalla,
    cambiar_nombre,
    obt_ruta_inicial)
from modulos.funciones import (
    ordenar, 
    traducir)

pygame.init()
pygame.mixer.init()
bip = pygame.mixer.Sound("./modulos/sonido/ping.mp3")

def main():
    while True:
        pantalla()
        # ruta_archivo = input("Ingresa la ruta del archivo a leer:\n > ")
        # ruta_archivo = ruta_archivo.replace('"', '')  # Eliminar comillas
        # obt_ruta_inicial()
        ordenar(obt_ruta_inicial())
        pantalla()
        mensaje = "Texto ordenado. Espere un momento a que se traduzca..."
        print(f"{mensaje:^71}")
        traducir("archivo_unido.txt")
        ordenar("texto_traducido.txt")
        os.remove("texto_traducido.txt")
        pantalla()
        pygame.mixer.Sound.play(bip)
        cambiar_nombre()
        pantalla()

        opcion_usuario = input("¿Desea realizar otra traduccion? (Y/N)\n > ")
        if opcion_usuario.lower() != "y":
            break

if __name__ == '__main__':
    main()