import csv
import json

# Cargar JSON
with open('productos_categoria_09.json', 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

# Cargar CSV
with open('productos_tienda.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_data = [row for row in csv_reader]

# Extraer los SKUs del CSV
csv_skus = {row[2] for row in csv_data}

# Filtrar JSON con SKUs coincidentes
matching_products = [item for item in json_data if item['sku'] in csv_skus]

# Guardar resultados en un nuevo archivo JSON
with open('productos_coincidentes9.json', 'w', encoding='utf-8') as output_file:
    json.dump(matching_products, output_file, ensure_ascii=False, indent=4)

print(f"Se encontraron {len(matching_products)} productos coincidentes.")
