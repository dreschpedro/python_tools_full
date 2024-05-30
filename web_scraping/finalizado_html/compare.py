import os
import pandas as pd
import json

# Función para leer múltiples archivos JSON desde un directorio
def read_json_files(directory, prefix):
    json_data = []
    for filename in os.listdir(directory):
        if filename.startswith(prefix) and filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                json_data.extend(data)  # Añadir los datos del archivo JSON a la lista
    return json_data

# Cargar el archivo CSV
csv_file_path = 'productos.csv'  # Reemplaza con la ruta de tu archivo CSV
csv_data = pd.read_csv(csv_file_path, header=None, names=['id', 'sku'])

# Leer todos los archivos JSON desde el directorio 'json_files' con el prefijo 'image_data'
json_directory = r'D:\REPOS\python_tools_full\web_scraping\finalizado_html'
json_prefix = 'image_data'  # Reemplaza con el prefijo de tus archivos JSON
all_json_data = read_json_files(json_directory, json_prefix)

# Convertir los SKUs del CSV a un diccionario con id como clave y sku como valor
csv_id_sku_dict = dict(zip(csv_data['id'], csv_data['sku']))

# Filtrar los datos JSON para incluir solo los SKUs que están en el CSV y añadir el id correspondiente
filtered_json_data = [{'id': id_, 'sku': csv_id_sku_dict[id_], 'image_url': entry['image_url']}
                      for entry in all_json_data
                      for id_ in csv_id_sku_dict.keys()
                      if entry['sku'] == csv_id_sku_dict[id_]]

# Guardar el resultado en un nuevo archivo JSON
output_json_file_path = 'resultado.json'  # Reemplaza con la ruta de tu archivo JSON de salida
with open(output_json_file_path, 'w') as outfile:
    json.dump(filtered_json_data, outfile, indent=4)

print(f'Se ha creado el archivo {output_json_file_path} con los datos filtrados.')
