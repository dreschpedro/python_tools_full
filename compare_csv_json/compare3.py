import csv
import json

def leer_json(ruta_json):
    with open(ruta_json) as archivo_json:
        return json.load(archivo_json)

def leer_csv(ruta_csv):
    with open(ruta_csv, newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        return list(lector_csv)

def comparar_json_csv(datos_json, datos_csv):
    coincidencias = []
    for producto_json in datos_json:
        sku_json = producto_json['sku']
        for fila_csv in reversed(datos_csv):
            sku_csv = fila_csv[-1]
            if sku_json == sku_csv:
                id_producto = fila_csv[0]
                imagen_urls = producto_json['image_urls']
                coincidencias.append({
                    'id': id_producto,
                    'sku': sku_json,
                    'image_urls': imagen_urls
                })
                break
    return coincidencias

def main(ruta_json, ruta_csv, ruta_salida):
    datos_json = leer_json(ruta_json)
    datos_csv = leer_csv(ruta_csv)
    coincidencias = comparar_json_csv(datos_json, datos_csv)
    
    # Escribir los datos en un archivo JSON
    with open(ruta_salida, 'w') as archivo_salida:
        json.dump(coincidencias, archivo_salida, indent=4)

ruta_json = 'productos_categoria_reposteria.json'
ruta_csv = 'productos_tienda.csv'
ruta_salida = 'coincidencias.json'

main(ruta_json, ruta_csv, ruta_salida)
