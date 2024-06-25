import json

# Cargar los archivos JSON
with open('data.json', 'r') as data_file:
    data = json.load(data_file)

with open('image_data.json', 'r') as image_data_file:
    image_data = json.load(image_data_file)

# Crear un diccionario para mapear los SKU a sus URLs de imagen
image_dict = {}
for item in image_data:
    sku = item['sku']
    image_url = item['image_url']
    if sku in image_dict:
        image_dict[sku].append(image_url)
    else:
        image_dict[sku] = [image_url]

# Crear una lista para guardar las coincidencias
result = []

# Buscar coincidencias
for product in data:
    sku = product['sku']
    if sku in image_dict:
        for image_url in image_dict[sku]:
            result.append({
                "nombre": product['nombre'],
                "sku": sku,
                "image_url": image_url
            })

# Guardar el resultado en un nuevo archivo JSON
with open('result.json', 'w') as result_file:
    json.dump(result, result_file, indent=4)

print("El archivo result.json se ha creado con éxito.")
