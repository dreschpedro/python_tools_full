import json

# Lee el archivo JSON
with open('productos_categoria_reposteria.json', 'r') as file:
    data = json.load(file)

# Cuenta cuántos productos hay
cantidad_productos = len(data)
print(f'El archivo JSON contiene {cantidad_productos} productos.')
