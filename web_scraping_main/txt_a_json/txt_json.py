import json

def leer_archivo(nombre_archivo):
    # Lee el archivo y devuelve un diccionario con el primer valor antes de la coma como clave
    # y el resto de la línea como valor
    datos = {}
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            partes = linea.strip().split(',')
            clave = int(partes[0])
            valor = ','.join(partes[1:])
            datos[clave] = valor
    return datos

def comparar_archivos(archivo1, archivo2):
    # Lee los datos de ambos archivos
    datos1 = leer_archivo(archivo1)
    datos2 = leer_archivo(archivo2)

    # Encuentra las coincidencias
    coincidencias = {}
    for clave, valor1 in datos1.items():
        if clave in datos2:
            valor2 = datos2[clave]
            coincidencias[clave] = {
                'id': clave,
                'nombre': valor1.split(',')[0],
                'sku': valor2.split(',')[1]
            }

    return coincidencias

archivo1 = 'formateado.txt'
archivo2 = 'productos_sku.txt'
resultado = comparar_archivos(archivo1, archivo2)

# Escribe el resultado en un nuevo archivo JSON
with open('resultado.json', 'w') as archivo_json:
    json.dump(list(resultado.values()), archivo_json, indent=2)

print("Se ha generado el archivo 'resultado.json' con las coincidencias encontradas.")
