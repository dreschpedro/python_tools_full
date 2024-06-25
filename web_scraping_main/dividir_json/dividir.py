import json
import math

def dividir_json_en_partes(ruta_archivo, num_partes):
    # Leer el archivo JSON completo
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    
    # Verificar si el JSON es una lista
    if not isinstance(datos, list):
        raise ValueError("El archivo JSON debe contener una lista en la raíz.")

    # Calcular el tamaño de cada parte
    tamaño_parte = math.ceil(len(datos) / num_partes)

    # Dividir la lista en partes más pequeñas
    partes = [datos[i:i + tamaño_parte] for i in range(0, len(datos), tamaño_parte)]

    # Guardar cada parte en un nuevo archivo JSON
    for i, parte in enumerate(partes):
        nombre_archivo_parte = f'parte_{i+1}.json'
        with open(nombre_archivo_parte, 'w', encoding='utf-8') as archivo_parte:
            json.dump(parte, archivo_parte, ensure_ascii=False, indent=4)
        print(f'Guardado {nombre_archivo_parte}')

# Ruta del archivo JSON original y número de partes deseadas
ruta_archivo = 'data.json'
num_partes = 6  # Ajusta este valor según el número de partes deseadas

dividir_json_en_partes(ruta_archivo, num_partes)