import json

def agregar_cero(sku):
    return str(sku).zfill(10)  # Asegura que el SKU tenga 10 dígitos, incluyendo ceros al inicio si es necesario

def comparar_json(archivo_pm_sku, archivo_data, archivo_salida):
    # Leer el archivo pm_sku.json
    with open(archivo_pm_sku, 'r', encoding='utf-8') as file:
        pm_sku_data = json.load(file)
    
    # Leer el archivo data.json
    with open(archivo_data, 'r', encoding='utf-8') as file:
        data_data = json.load(file)
    
    # Crear un conjunto de SKUs desde pm_sku_data para comparación rápida
    pm_skus = {item['sku'] for item in pm_sku_data}
    
    # Encontrar los elementos en data_data cuyos SKUs no están en pm_skus
    no_coinciden = [
        {'sku': agregar_cero(item['sku']), 'nombre': item['nombre']}
        for item in data_data
        if agregar_cero(item['sku']) not in pm_skus
    ]
    
    # Escribir los resultados en un nuevo archivo JSON
    with open(archivo_salida, 'w', encoding='utf-8') as file:
        json.dump(no_coinciden, file, ensure_ascii=False, indent=4)

# Archivos JSON
archivo_pm_sku = 'pm_sku.json'
archivo_data = 'data.json'
archivo_salida = 'resultado_no_coinciden.json'

# Comparar los archivos y guardar los resultados
comparar_json(archivo_pm_sku, archivo_data, archivo_salida)

print(f'Resultados guardados en {archivo_salida}')
