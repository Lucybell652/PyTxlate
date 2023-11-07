# Python Traduccion/Lectura (PyTxLate)

## Descripción 👌
PyTxLate es un programa en consola que organiza un texto y luego lo traduce al español. Actualmente solo se hace la traduccion al español por razones personales. El código está estructurado en varios módulos para mantenerlo organizado y modular.

## Requisitos 💻
1. Python 3.x
2. Bibliotecas:
   - deep_translator
   - pygame
   - art

## Uso 👩‍💻
En consola:
1. Ejecuta `main.py` para iniciar el programa.
2. Se te pedirá ingresar la ruta del archivo. No importa si lo ingresas con comillas.
3. El programa primero organizará el texto, creando un archivo `archivo_unido.txt`
4. Despues tomará el archivo y lo traducirá, creando un archivo `texto_traducido.txt`
5. El archivo traducido estará desordenado nuevamente, ya que se realiza un corte cada 500 caracteres (con ciertas especificaciones) por lo que se necesita ordenar nuevamente
6. El programa vuelve a ordenar el archivo pero el traducido, creando nuevamente el archivo `archivo_unido` y elimina `texto_traducido.txt`
7. Al finalizar todo, se reproducira un pequeño pitido, indicando la finalizacion de la traducción.
8. Se le pedirá que ingrese un nombre para el archivo, guardandose en .txt en la carpeta descargas dentro de la subcarpeta `traducciones`
9. Se le preguntará si desea realizar una nueva traduccion, caso contrario cierra el programa.

## Estructura del Código 💻
- `main.py`: Este es el punto de entrada del programa. Controla la interfaz de usuario y llama a las funciones de ordenado y traducción.
- `modulos/sistema.py`: Contiene funciones para la gestión de la consola, limpieza de nombres de archivos y obtención de rutas de destino.
- `modulos/funciones.py`: Contiene funciones para la organización del archivo y la traducción del mismo.
- `modulos/sonido/ping.mp3`: El archivo mp3 que se reproduce una vez termine la traducción y aviso para ingresar el nuevo nombre del archivo.

## Personalización 🖖
- Puedes personalizar las carpetas de destino modificando las funciones `ruta_fin_traducido()`.
- Puedes personalizar el comportamiento de las funciones de traducción agregando opciones adicionales desde `modulos/funciones.py`.

## Notas Importantes ‼️
- Este programa se basa en bibliotecas de terceros y utiliza la API de Google Traductor para la traducción del texto.
- El programa utiliza la biblioteca "art" para imprimir un título decorativo en la consola. Asegúrate de tener esta biblioteca instalada para obtener una mejor experiencia visual.
- Se usa "pygame", importante para la reproducción del sonido de aviso.

## Errores detectados 😓
- Aun no existe un correcto control de errores del usuario.

## Futuras actualizaciones ♥️
- Mejorar el manejo de errores.
- Crear una interfaz grafica.

Espero que este programa te sea tan útil como lo es para mí. Disfrutalo. 
