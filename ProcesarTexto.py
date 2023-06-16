import string

def procesar(archivo):
    # Abrir el archivo en modo lectura
    with open(archivo, "r", encoding="utf-8") as file:
        # Leer el contenido del archivo
        contenido = file.read()

    # Definir los reemplazos de las tildes
    reemplazos = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "Á": "A",
        "É": "E",
        "Í": "I",
        "Ó": "O",
        "Ú": "U"
    }

    # Realizar los reemplazos en el contenido
    contenido = "".join(reemplazos.get(c, c) for c in contenido)

    # Convertir el contenido a mayúsculas
    contenido = contenido.upper()

    # Realizar las sustituciones
    contenido = contenido.replace('A', 'I')
    contenido = contenido.replace('H', 'J')
    contenido = contenido.replace('Ñ', 'N')
    contenido = contenido.replace('K', 'L')
    contenido = contenido.replace('V', 'U')
    contenido = contenido.replace('W', 'V')
    contenido = contenido.replace('Z', 'Y')
    contenido = contenido.replace('R', 'F')

    # Definir los signos de puntuación adicionales del alfabeto español
    signos_adicionales = "¡¿"

    # Definir los caracteres de puntuación
    caracteres_puntuacion = string.punctuation + signos_adicionales
    

    # Eliminar los signos de puntuación del contenido
    contenido = "".join(c for c in contenido if c not in caracteres_puntuacion)

    # Eliminar los espacios en blanco y saltos del contenido
    contenido = contenido.replace(" ", "") 
    contenido = contenido.replace("\n", "") 

    print("Longitud del texto: ",len(contenido))
    # Abrir el archivo en modo escritura
    with open("POEMA_PRE.txt", "w", encoding="utf-8") as file:
        # Escribir el contenido sin tildes en el archivo
        file.write(contenido)


# Ejemplo de uso
archivo = "POEMA.txt"
procesar(archivo)
print("\nArchivo POEMA.txt fue procesado, el nuevo archivo es POEMA_PRE.txt")
