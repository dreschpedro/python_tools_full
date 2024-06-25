import json

# Leer el archivo productos_seleccionados.json
with open('productos_seleccionados.json', 'r', encoding='utf-8') as json_file:
    productos_data = json.load(json_file)

# Leer el archivo id_sku.txt y almacenar los SKUs en un diccionario
sku_to_id = {}
with open('id_sku.txt', 'r', encoding='utf-8') as txt_file:
    for line in txt_file:
        id_sku = line.strip().split(',')
        if len(id_sku) == 2:
            sku_to_id[id_sku[1]] = id_sku[0]

# Lista para almacenar los productos que coinciden
productos_coincidentes = []

# Comparar los SKUs y guardar los productos coincidentes
for producto in productos_data:
    if producto['sku'] in sku_to_id:
        producto_coincidente = {
            'id': sku_to_id[producto['sku']],
            'sku': producto['sku'],
            'nombre': producto['nombre'],
            'images': producto['images']
        }
        productos_coincidentes.append(producto_coincidente)

# Escribir los productos coincidentes en un nuevo archivo JSON
with open('productos_coincidentes_con_id.json', 'w', encoding='utf-8') as output_file:
    json.dump(productos_coincidentes, output_file, ensure_ascii=False, indent=2)

print(f'Se han encontrado {len(productos_coincidentes)} productos coincidentes.')
    