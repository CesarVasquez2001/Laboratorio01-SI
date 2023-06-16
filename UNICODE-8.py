# Abrir el archivo de texto
nombre_archivo = "POEMA_PRE.txt"
with open(nombre_archivo, "r") as archivo:
    contenido = archivo.read()

# Volver a preprocesar el contenido según UNICODE-8
contenido_preprocesado = ""
for caracter in contenido:
    unicode_8 = ord(caracter)  # Obtener el valor UNICODE-8 del carácter
    contenido_preprocesado += str(unicode_8) + " "  # Agregar el valor UNICODE-8 al contenido preprocesado

# Guardar el contenido preprocesado en un nuevo archivo
nombre_archivo_preprocesado = "POEMA_UNICODE-8.txt"
with open(nombre_archivo_preprocesado, "w") as archivo_preprocesado:
    archivo_preprocesado.write(contenido_preprocesado)

print("Archivo preprocesado guardado correctamente.")
