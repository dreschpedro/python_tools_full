import csv
import json

# Cargar CSV
csv_filename = 'productos_tienda.csv'
json_filename = 'productos_coincidentes01.json'
output_filename = 'resultados_finales.json'

with open(csv_filename, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_data = [{ "id": row[0], "sku": row[2] } for row in csv_reader]

# Cargar el JSON
with open(json_filename, 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

# Crear un diccionario de SKUs del JSON para una búsqueda rápida
json_sku_dict = {item['sku']: item['nombre'] for item in json_data}

# Filtrar CSV con SKUs coincidentes y extraer nombres del JSON
matching_entries = [
    {
        "id": entry["id"],
        "sku": entry["sku"],
        "nombre": json_sku_dict[entry["sku"]]
    }
    for entry in csv_data
    if entry["sku"] in json_sku_dict
]

# Guardar los resultados en un nuevo archivo JSON
with open(output_filename, 'w', encoding='utf-8') as output_file:
    json.dump(matching_entries, output_file, ensure_ascii=False, indent=4)

print(f"Se encontraron {len(matching_entries)} entradas coincidentes.")