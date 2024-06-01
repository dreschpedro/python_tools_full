import json
from collections import defaultdict

# Leer el archivo JSON
with open('productos_categoria_01.json', 'r') as file:
    data = json.load(file)

# Crear un diccionario para agrupar las URLs de las imágenes por SKU
sku_dict = defaultdict(list)

for item in data:
    sku = item['sku']
    sku = item['id']
    sku = item['sku']
    image_url = item['image_url']
    sku_dict[sku].append(image_url)

# Convertir el diccionario a una lista de diccionarios con el formato deseado
grouped_data = [{'sku': sku, 'image_urls': urls} for sku, urls in sku_dict.items()]

# Guardar los resultados en un nuevo archivo JSON
with open('agrupado_por_sku.json', 'w') as outfile:
    json.dump(grouped_data, outfile, indent=4)

print("El archivo ha sido agrupado y guardado exitosamente.")
