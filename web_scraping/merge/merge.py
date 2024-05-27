import json

# Cargar los datos desde los archivos JSON
with open('image_data.json', 'r') as f:
    image_data = json.load(f)

with open('velas_copy.json', 'r') as f:
    productos = json.load(f)

# Crear un diccionario para acceder rápidamente a las URLs de las imágenes por SKU
image_dict = {item['sku']: item['image_url'] for item in image_data}

# Lista para almacenar los resultados combinados
result = []

# Recorrer la lista de productos y buscar coincidencias en el diccionario de imágenes
for producto in productos:
    sku = producto['sku']
    if sku in image_dict:
        combined_entry = {
            'id': producto['id'],
            'sku': sku,
            'nombre': producto['nombre'],
            'image_url': image_dict[sku]
        }
        result.append(combined_entry)

# Guardar los resultados en un nuevo archivo JSON
with open('combined_data.json', 'w') as f:
    json.dump(result, f, indent=4)

print("Datos combinados guardados en 'combined_data.json'")
