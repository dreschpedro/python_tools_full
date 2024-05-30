import csv
import json

# Abrir el archivo CSV
with open('productos_sin_imagen.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Saltar la primera línea si tiene encabezados
    skus = [row[1] for row in csv_reader]  # Obtener los SKUs del CSV

# Abrir el archivo JSON
with open('productos_categoria_90.json', mode='r') as json_file:
    productos = json.load(json_file)

# Comparar los SKUs y crear un nuevo JSON con los resultados
resultados = []
for producto in productos:
    if producto['sku'] in skus:
        resultados.append({
            'id': producto['id'],
            'nombre': producto['nombre'],
            'sku': producto['sku'],
            'image_url': producto['image_url']
        })

# Escribir el nuevo JSON
with open('resultados.json', mode='w') as json_file:
    json.dump(resultados, json_file, indent=4)