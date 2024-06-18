import json

# Función para leer el archivo imagenes.json
def read_imagenes_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Función para leer el archivo id_sku.txt
def read_id_sku_txt(file_path):
    id_sku_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                id_sku_parts = line.split(',')
                if len(id_sku_parts) == 2:
                    id_sku_data.append((id_sku_parts[0], id_sku_parts[1]))
    return id_sku_data

# Función para comparar y obtener los registros coincidentes
def find_matching_records(imagenes_data, id_sku_data):
    matching_records = []
    for img_record in imagenes_data:
        for id_sku_record in id_sku_data:
            if img_record['sku'] == id_sku_record[1]:
                matching_records.append({
                    'id': id_sku_record[0],
                    'sku': img_record['sku'],
                    'nombre': img_record['nombre'],
                    'image_url': img_record['image_url']
                })
    return matching_records

# Función para escribir los registros coincidentes en un nuevo archivo JSON
def write_matching_records_to_json(records, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(records, file, indent=4)

# Rutas de los archivos de entrada y salida
imagenes_file = 'imagenes.json'
id_sku_file = 'id_sku.txt'
output_file = 'registros_coincidentes.json'

# Leer los datos de los archivos
imagenes_data = read_imagenes_json(imagenes_file)
id_sku_data = read_id_sku_txt(id_sku_file)

# Encontrar registros coincidentes
matching_records = find_matching_records(imagenes_data, id_sku_data)

# Escribir los registros coincidentes en un nuevo archivo JSON
write_matching_records_to_json(matching_records, output_file)

print(f"Se han guardado los registros coincidentes en el archivo: {output_file}")
