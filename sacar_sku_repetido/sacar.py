import json

# Cargar los datos desde el archivo JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Crear un conjunto para almacenar los productos únicos
unique_products = {}

# Iterar sobre los productos en los datos
for product in data:
    # Crear una clave única usando el SKU
    key = product['sku']
    if key not in unique_products:
        unique_products[key] = product

# Crear una lista con los nombres y SKUs únicos
result = [{'nombre': product['nombre'], 'sku': product['sku']} for product in unique_products.values()]

# Imprimir el resultado
# print(json.dumps(result, indent=4))

# Guardar el resultado en un archivo JSON si es necesario
with open('unique_products.json', 'w') as file:
    json.dump(result, file, indent=4)
