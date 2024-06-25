import json

# Cargar el JSON
with open('productos.json', 'r') as f:
    productos_json = json.load(f)

# Leer el archivo coincidencias.txt y almacenar las coincidencias en un diccionario
coincidencias = {}
with open('coincidencias.txt', 'r') as f:
    for line in f:
        sku, id_sku = line.strip().split(',')
        coincidencias[sku] = id_sku

# Modificar el JSON agregando el ID del producto a cada componente
for sku, data in productos_json.items():
    if sku in coincidencias:
        id_producto = coincidencias[sku]
        data['id_producto'] = id_producto  # Agregar ID al producto padre
        for componente in data['Componentes']:
            sub_sku = componente['SKU']
            if sub_sku in coincidencias:
                componente['id_producto'] = coincidencias[sub_sku]

# Guardar el JSON modificado en un nuevo archivo
with open('productos_modificado.json', 'w') as f:
    json.dump(productos_json, f, indent=4)
