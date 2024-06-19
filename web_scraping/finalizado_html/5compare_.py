import json

# Cargar el archivo JSON
with open('productos_seleccionados.json', 'r') as file:
    productos_seleccionados = json.load(file)

# Cargar el archivo de texto y crear un diccionario para facilitar la búsqueda
sku_to_id = {}
with open('id_sku.txt', 'r') as file:
    for line in file:
        id, sku = line.strip().split(',')
        sku_to_id[sku] = id

# Comparar los SKU y crear la lista de coincidencias
resultados = []
for producto in productos_seleccionados:
    sku = producto['sku']
    if sku in sku_to_id:
        coincidencia = {
            "sku": sku,
            "nombre": producto['nombre'],
            "id": sku_to_id[sku],
            "images": producto['images']
        }
        resultados.append(coincidencia)

# Guardar el resultado en un archivo JSON
with open('resultados.json', 'w') as file:
    json.dump(resultados, file, indent=4)

print("Proceso completado. Los resultados se han guardado en 'resultados.json'.")
