import json

# Leer el archivo de texto y cargar los datos en una lista de diccionarios
id_sku_list = []
with open('id_sku.txt', 'r') as file:
    for line in file:
        id, sku = line.strip().split(',')
        id_sku_list.append({"id": id, "sku": sku})

# Leer el archivo JSON
with open('imagenes.json', 'r') as file:
    imagenes_data = json.load(file)

# Crear una lista para almacenar los resultados
resultados = []

# Crear un diccionario de imágenes con el SKU como clave para una búsqueda rápida
imagenes_dict = {producto['sku']: producto['images'] for producto in imagenes_data}

# Comparar los SKUs y generar el resultado
for item in id_sku_list:
    sku = item['sku']
    if sku in imagenes_dict:
        resultado = {
            'sku': sku,
            'id': item['id'],
            'images': imagenes_dict[sku]
        }
        resultados.append(resultado)

# Guardar los resultados en un nuevo archivo JSON
with open('resultados.json', 'w') as file:
    json.dump(resultados, file, indent=4)

print("Archivo 'resultados.json' creado con éxito.")
