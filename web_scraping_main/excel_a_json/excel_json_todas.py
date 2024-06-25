import pandas as pd
import json

nombre_archivo = 'productos.xlsx'  # Reemplaza con el nombre de tu archivo Excel
#nombre_hoja = input('Nombre de la hoja del excel: ')

# Leer todas las hojas del archivo Excel
excel_data_dict = pd.read_excel(nombre_archivo, sheet_name=None)

# Inicializar una lista para almacenar todos los datos de todas las hojas
all_data = []

# Iterar sobre todas las hojas del archivo Excel
for nombre_hoja, datos_hoja in excel_data_dict.items():
    # Convertir los datos de la hoja actual a formato JSON
    thisisjson = datos_hoja.to_json(orient='records')
    # Convertir el JSON a un diccionario Python
    thisisjson_dict = json.loads(thisisjson)
    # Extender la lista 'all_data' con los datos de la hoja actual
    all_data.extend(thisisjson_dict)

# Definir el archivo donde se escribirán los datos y abrirlo en modo escritura ('w')
with open('data.json', 'w', encoding='UTF-8') as json_file:
    # Escribir el JSON final (todos los datos de todas las hojas) en el archivo
    json.dump(all_data, json_file)

print('Se ha creado el archivo data.json con los datos de todas las hojas del Excel.')
