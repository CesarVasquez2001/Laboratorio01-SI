nombre_archivo = "POEMA_ALFABETO.txt"
with open(nombre_archivo, "r") as archivo:
    contenido = archivo.read()

# Insertar la cadena "UNSA" cada 26 caracteres
contenido_preprocesado = ""
for i, caracter in enumerate(contenido):
    contenido_preprocesado += caracter
    if (i + 1) % 26 == 0:
        contenido_preprocesado += "UNSA"

# Calcular la longitud del contenido preprocesado
longitud = len(contenido_preprocesado)

# Calcular la cantidad de caracteres "#" a agregar para que sea múltiplo de 5
relleno = (5 - longitud % 5) % 5

# Agregar caracteres "#" al final si es necesario
contenido_preprocesado += "#" * relleno

# Guardar el contenido preprocesado en un nuevo archivo
nombre_archivo_preprocesado = "POEMA_UNSA.txt"

print("Longitud del nuevo texto es: ",len(contenido_preprocesado))

with open(nombre_archivo_preprocesado, "w") as archivo_preprocesado:
    archivo_preprocesado.write(contenido_preprocesado)

print("\nArchivo POEMA_ALFABETO.txt fue procesado, el nuevo archivo es POEMA_UNSA.txt")
