import json

# Leer el archivo .txt
txt_file = 'id_sku.txt'
with open(txt_file, 'r') as f:
    txt_data = [line.strip().split(',') for line in f]

# Leer el archivo .json
json_file = 'product_compositions.json'
with open(json_file, 'r') as f:
    json_data = json.load(f)

# Crear un diccionario para almacenar los IDs de SKU y ComponentSKUCode
sku_id_map = {sku: id_value for id_value, sku in txt_data}

# Función para agregar el id a la estructura del JSON si hay coincidencias
def add_id_to_json():
    for product in json_data:
        sku = product['SKU']
        if sku in sku_id_map:
            product['ID'] = sku_id_map[sku]
        for component in product['ProductComposition']:
            component_sku_code = component['ComponentSKUCode']
            if component_sku_code in sku_id_map:
                component['ID'] = sku_id_map[component_sku_code]

# Llamar la función para agregar los IDs
add_id_to_json()

# Guardar los resultados en un nuevo archivo .json
result_file = 'resultado.json'
with open(result_file, 'w') as f:
    json.dump(json_data, f, indent=4)

print(f'Resultados guardados en {result_file}')
