import json

# Leer el archivo JSON
with open('productos.json', 'r') as json_file:
    json_data = json.load(json_file)
    json_skus = {item['SKUCode'] for item in json_data}

# Leer el archivo de texto
with open('skus.txt', 'r') as txt_file:
    txt_skus = {line.strip() for line in txt_file}

# Encontrar los SKUs que coinciden
matching_skus = json_skus.intersection(txt_skus)

# Imprimir los SKUs coincidentes
print("SKUs coincidentes:")
for sku in matching_skus:
    print(sku)