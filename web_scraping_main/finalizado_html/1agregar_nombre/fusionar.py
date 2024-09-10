import json

# Cargar los archivos JSON
with open('sku_imagen.json', 'r') as file:
    sku_imagen = json.load(file)

with open('sku_nombre.json', 'r') as file:
    sku_nombre = json.load(file)

# Crear un diccionario para buscar el nombre por SKU, asegurando que tenga un 0 adelante
sku_to_nombre = {f"{item['sku']:010}": item['nombre'] for item in sku_nombre}

# Crear la lista de salida combinada
combined_data = []

for item in sku_imagen:
    sku = f"{item['sku']:010}"  # Asegura que el SKU tenga un 0 adelante
    if sku in sku_to_nombre:
        combined_data.append({
            'sku': sku,
            'nombre': sku_to_nombre[sku],
            'image_url': item['image_url']
        })

# Guardar el resultado en un nuevo archivo JSON
with open('sku_combined.json', 'w') as output_file:
    json.dump(combined_data, output_file, indent=4)

print("Archivo combinado guardado como 'sku_combined.json'")
