import os
from deep_translator import GoogleTranslator

def cls(): # Limpiar consola
    os.system('cls')

def ordenar(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:  # Especifica la codificación utf-8 al abrir el archivo
        lineas = archivo.readlines()

    lineas = [linea.rstrip() for linea in lineas]  # Elimina el "\n" al final de cada línea
    texto_unido = ' '.join(lineas)  # Une todas las líneas en una sola cadena
    texto_separado = texto_unido.split(". ")

    with open('archivo_unido.txt', 'w', encoding='utf-8') as archivo_unido:
        archivo_unido.write("\n".join(texto_separado))

def traducir(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo_traducir:
        texto_a_traducir = archivo_traducir.read()

    fragmentos = []
    fragmento_actual = ""
    for palabra in texto_a_traducir.split():
        if len(fragmento_actual) + len(palabra) <= 500:
            fragmento_actual += palabra + " "
        else:
            fragmentos.append(fragmento_actual.rstrip())
            fragmento_actual = palabra + " "
    if fragmento_actual:
        fragmentos.append(fragmento_actual.rstrip())

    with open("texto_traducido.txt", 'w', encoding='utf-8') as archivo_traducido:
        for fragmento in fragmentos:
            fragmento_traducido = GoogleTranslator(source='auto', target='es').translate(fragmento)
            archivo_traducido.write(fragmento_traducido + "\n")

    os.remove("archivo_unido.txt")

def cambiar_nombre():
    ruta_traducido = "archivo_unido.txt"
    ruta_nuevo_nombre = os.path.join(ruta_fin_traducido(), input("Ingrese el nombre de su archivo\n> ") + ".txt")
    os.rename(ruta_traducido, ruta_nuevo_nombre)

def ruta_fin_traducido():
    descargas_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    carpeta_traducciones = os.path.join(descargas_path, 'traducciones') 
    if not os.path.exists(carpeta_traducciones):
        os.makedirs(carpeta_traducciones)
    return carpeta_traducciones

if __name__ == '__main__':
    ruta_archivo = input("Ingresa la ruta del archivo a leer:\n > ")
    ruta_archivo = ruta_archivo.replace('"', '')  # Eliminar comillas
    ordenar(ruta_archivo)
    cls()
    print("Se ha ordenado el texto\nEspere un momento a que se traduzca...")
    traducir("archivo_unido.txt")
    ordenar("texto_traducido.txt")
    os.remove("texto_traducido.txt")
    cls()
    cambiar_nombre()
