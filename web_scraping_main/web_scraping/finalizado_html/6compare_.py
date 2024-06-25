import json

# Cargar el archivo registros_coincidentes.json
with open('registros_coincidentes.json', 'r') as file:
    registros_coincidentes = json.load(file)

# Cargar el archivo productos_seleccionados.json
with open('productos_seleccionados.json', 'r') as file:
    productos_seleccionados = json.load(file)

# Crear un conjunto de SKU de los productos seleccionados para una búsqueda rápida
productos_sku_set = {producto['sku'] for producto in productos_seleccionados}

# Filtrar los registros que no coinciden
no_coincidentes = []
for registro in registros_coincidentes:
    sku = registro['sku']
    if sku not in productos_sku_set:
        no_coincidentes.append(registro)

# Guardar el resultado en un archivo JSON
with open('registros_no_coincidentes.json', 'w') as file:
    json.dump(no_coincidentes, file, indent=4)

print("Proceso completado. Los registros no coincidentes se han guardado en 'registros_no_coincidentes.json'.")
