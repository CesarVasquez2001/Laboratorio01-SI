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

archivo_salida = "POEMA_PRE.txt"

trigramas, posiciones, distancias = encontrar_trigramas_y_distancias(archivo_salida)
print("Trigramas repetidos:")
for trigrama, frecuencia in trigramas.items():
    print(f"{trigrama}: {frecuencia} veces")

print("\nPosiciones de los trigramas:")
for trigrama, pos in posiciones.items():
    print(f"{trigrama}: {pos}")

print("\nDistancias entre trigramas iguales:")
for trigrama, dist in distancias.items():
    print(f"{trigrama}: {dist}")
