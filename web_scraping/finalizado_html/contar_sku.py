import json

# Cargar el archivo JSON
with open('productos_categoria_01.json', 'r') as file:
    productos = json.load(file)

# Crear un conjunto para almacenar los SKUs únicos
skus_unicos = set()

# Iterar sobre los productos y añadir los SKUs al conjunto
for producto in productos:
    skus_unicos.add(producto['sku'])

# Contar el número de SKUs únicos
num_productos_unicos = len(skus_unicos)

print(f"El número de productos únicos es: {num_productos_unicos}")
