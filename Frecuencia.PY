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

