# # COINCIDENTES
# import csv
# import json

# # Abrir el archivo CSV
# with open('productos_sin_imagen.csv', mode='r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader)  # Saltar la primera línea si tiene encabezados
#     skus = [row[1] for row in csv_reader]  # Obtener los SKUs del CSV

# # Abrir el archivo JSON
# with open('productos_categoria_01.json', mode='r') as json_file:
#     productos = json.load(json_file)

# # Comparar los SKUs y crear un nuevo JSON con los resultados
# resultados = []
# for producto in productos:
#     if producto['sku'] in skus:
#         resultados.append({
#             'id': producto['id'],
#             'nombre': producto['nombre'],
#             'sku': producto['sku'],
#             'image_url': producto['image_url']
#         })

# # Escribir el nuevo JSON
# with open('resultados.json', mode='w') as json_file:
#     json.dump(resultados, json_file, indent=4)



# NO COINCIDENTES
import csv
import json

# Leer el archivo CSV y obtener los SKUs únicos
with open('productos_sin_imagen.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Saltar la primera línea si tiene encabezados
    csv_rows = list(csv_reader)  # Leer todas las filas del CSV
    skus_csv = {row[2] for row in csv_rows}  # Obtener los SKUs del CSV como un conjunto (último valor después de la 2da coma)

# Leer el archivo JSON y obtener los SKUs
with open('productos_categoria_01.json', mode='r') as json_file:
    productos = json.load(json_file)
    skus_json = {producto['sku'] for producto in productos}  # Obtener los SKUs del JSON como un conjunto

# Encontrar los SKUs que están en el CSV pero no en el JSON
skus_no_encontrados = skus_csv - skus_json

# Escribir las filas del CSV cuyos SKUs no están en el JSON
with open('skus_no_encontrados.csv', mode='w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    headers = ["ID", "Nombre", "SKU"]  # Especificar los encabezados del archivo de salida
    csv_writer.writerow(headers)  # Escribir los encabezados

    written_rows = set()  # Conjunto para almacenar las filas ya escritas

    for row in csv_rows:
        if row[2] in skus_no_encontrados:
            row_tuple = tuple(row)  # Convertir la fila a una tupla para almacenarla en el conjunto
            if row_tuple not in written_rows:
                csv_writer.writerow(row)
                written_rows.add(row_tuple)  # Añadir la fila al conjunto de filas escritas

print(f"Líneas con SKUs no encontrados guardadas en 'skus_no_encontrados.csv'")
