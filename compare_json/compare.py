import json

# Cargar los archivos JSON
with open('data.json', 'r') as file:
    data = json.load(file)

with open('productos_categoria_01.json', 'r') as file:
    productos_categoria = json.load(file)

# Crear un diccionario para almacenar los resultados
resultados = []

# Crear un diccionario de productos con el SKU como clave para una búsqueda rápida
productos_dict = {producto['sku']: producto for producto in data}

# Recorrer los productos de la categoría y buscar coincidencias por SKU
for producto in productos_categoria:
    sku = producto['sku']
    if sku in productos_dict:
        # Añadir la coincidencia al resultado
        resultado = {
            'sku': sku,
            'nombre': productos_dict[sku]['nombre'],
            'image_url': producto['image_url']
        }
        resultados.append(resultado)

# Guardar los resultados en un nuevo archivo JSON
with open('resultados.json', 'w') as file:
    json.dump(resultados, file, indent=4)

print("Archivo 'resultados.json' creado con éxito.")
