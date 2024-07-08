import json

def compare_and_generate_json(txt_file, json_file, output_json_file):
    # Leer el archivo de texto y obtener los SKUs únicos
    with open(txt_file, 'r') as file:
        txt_lines = file.readlines()
    
    skus = {line.split(',')[1].strip() for line in txt_lines}  # Obtener el segundo elemento (SKU) de cada línea

    # Leer el archivo JSON
    with open(json_file, 'r') as file:
        json_data = json.load(file)
    
    result = []

    # Comparar los SKUs del archivo de texto con los del archivo JSON
    for product in json_data:
        if product["SKUCode"] in skus:
            result.append({
                "SKU": product["SKUCode"],
                "ProductComposition": product["ProductComposition"]
            })
    
    # Escribir el resultado en un nuevo archivo JSON
    with open(output_json_file, 'w') as file:
        json.dump(result, file, indent=4)

# Archivos de entrada y salida
txt_file = 'output.txt'  # Archivo de texto resultante de la ejecución anterior
json_file = 'productos.json'  # Archivo JSON proporcionado
output_json_file = 'result.json'  # Archivo JSON resultante

# Comparar y generar archivo JSON resultante
compare_and_generate_json(txt_file, json_file, output_json_file)
