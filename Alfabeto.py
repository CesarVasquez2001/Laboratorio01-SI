# Abrir el archivo de texto
nombre_archivo = "POEMA_UNICODE-8.txt"
with open(nombre_archivo, "r") as archivo:
    contenido = archivo.read()

valores = contenido.split()  # Separar los valores utilizando el espacio como separador
valores = [int(valor) for valor in valores]  # Convertir los valores a enteros

# Volver a preprocesar el contenido según UNICODE-8
contenido_preprocesado = ""
for caracter in valores:
    alfabeto = chr(caracter)  # Convertir el valor UNICODE-8 al carácter alfabético correspondiente
    contenido_preprocesado += alfabeto

# Guardar el contenido preprocesado en un nuevo archivo
nombre_archivo_preprocesado = "POEMA_ALFABETO.txt"
with open(nombre_archivo_preprocesado, "w") as archivo_preprocesado:
    archivo_preprocesado.write(contenido_preprocesado)

print("Archivo unicode-8 convertido a texto segun alfabeto guardado correctamente.")
