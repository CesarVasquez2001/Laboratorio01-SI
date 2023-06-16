import string

def normalize(archivo):
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

    print("Longitud: ",len(contenido))
    # Abrir el archivo en modo escritura
    with open("POEMA_PRE.txt", "w", encoding="utf-8") as file:
        # Escribir el contenido sin tildes en el archivo
        file.write(contenido)


def frecuencias(archivo):
    # Inicializar un diccionario para almacenar las frecuencias
    tabla_frecuencias = {}

    # Abrir el archivo en modo lectura
    with open(archivo, "r") as file:
        # Leer el contenido del archivo
        contenido = file.read()

    # Recorrer cada letra de la 'A' a la 'Z'
    for letra in range(ord('A'), ord('Z') + 1):
        letra_actual = chr(letra)
        # Calcular la frecuencia de la letra en el texto
        frecuencia = contenido.count(letra_actual)
        # Agregar la letra y su frecuencia al diccionario
        tabla_frecuencias[letra_actual] = frecuencia

    return tabla_frecuencias

def encontrar_trigramas_y_distancias(archivo):
     # Abrir el archivo en modo lectura
    with open(archivo, "r") as file:
        # Leer el contenido del archivo
        texto = file.read()
    
    trigramas = {}
    posiciones = {}
    distancias = {}
    
    indice = 0
    while indice < len(texto) - 2:
        trigrama = texto[indice:indice+3]
        
        # Verificar si el trigrama ya existe
        if trigrama in trigramas:
            trigramas[trigrama] += 1
            posiciones[trigrama].append(indice)
            
            # Calcular la distancia con el trigrama anterior
            distancia = indice - posiciones[trigrama][-2] - 3
            distancias[trigrama].append(distancia)
        else:
            trigramas[trigrama] = 1
            posiciones[trigrama] = [indice]
            distancias[trigrama] = []
        
        indice += 1
        
    trigramas_repetidos = {trigrama: frecuencia for trigrama, frecuencia in trigramas.items() if frecuencia > 1}
    posiciones_repetidas = {trigrama: posiciones[trigrama] for trigrama in trigramas_repetidos}
    distancias_repetidas = {trigrama: distancias[trigrama] for trigrama in trigramas_repetidos}
    
    return trigramas_repetidos, posiciones_repetidas, distancias_repetidas

 

# Ejemplo de uso
archivo = "POEMA.txt"

normalize(archivo)

archivo_salida = "POEMA_PRE.txt"
tabla = frecuencias(archivo_salida)

# Ordenar las frecuencias de mayor a menor
frecuencias_ordenadas = sorted(tabla.items(), key=lambda x: x[1], reverse=True)

# Obtener los cinco caracteres de mayor frecuencia
caracteres_mayor_frecuencia = [letra for letra, frecuencia in frecuencias_ordenadas[:5]]

print("Tabla de frecuencias:")
for letra, frecuencia in frecuencias_ordenadas:
    print(f"{letra}: {frecuencia}")

print("Los cinco caracteres de mayor frecuencia son:", caracteres_mayor_frecuencia)

