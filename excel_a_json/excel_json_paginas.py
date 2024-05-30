import pandas as pd
import json

# nombre_archivo = input('Nombre del archivo (sin extensión): ')
nombre_archivo = 'productos'

# Cargar el archivo Excel
excel_file = pd.ExcelFile(f'{nombre_archivo}.xlsx')

# Listar los nombres de las hojas del archivo Excel
print('Nombres de las hojas del archivo Excel:')
for sheet_name in excel_file.sheet_names:
    print(sheet_name)
