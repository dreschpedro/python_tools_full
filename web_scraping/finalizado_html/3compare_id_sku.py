import json

# Leer el archivo id_sku.txt
with open('id_sku.txt', 'r') as f:
    id_sku_lines = f.readlines()

# Procesar el archivo id_sku.txt en un diccionario
id_sku_dict = {}
for line in id_sku_lines:
    line = line.strip()
    if line:
        id, sku = line.split(',')
        id_sku_dict[sku] = id

# Leer el archivo agrupado_por_sku.json
with open('coincidencias2.json', 'r') as f:
    grouped_data = json.load(f)

# Buscar coincidencias y crear el resultado
result = []
for item in grouped_data:
    sku = item['sku']
    if sku in id_sku_dict:
        result.append({
            'id': id_sku_dict[sku],
            'sku': sku,
            'image_urls': item['image_urls']
        })

# Guardar el resultado en un nuevo archivo JSON
with open('coincidencias22.json', 'w') as f:
    json.dump(result, f, indent=4)

print("Las coincidencias han sido guardadas en coincidencias.json")
