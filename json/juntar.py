import pandas as pd
import json

# Cargar el archivo Excel
archivo_excel = 'REPOSTERIA_CAMBIO_NOMBRE.xlsx'  # Cambia esto al nombre del archivo que subas
excel = pd.ExcelFile(archivo_excel)

# Leer todas las hojas y combinarlas en un solo DataFrame
dataframes = []
for hoja in excel.sheet_names:
    df = pd.read_excel(archivo_excel, sheet_name=hoja, header=None, usecols=[0, 1])  # Leer solo las dos primeras columnas
    df.columns = ['sku', 'nombre']  # Renombrar las columnas
    dataframes.append(df)

# Concatenar todos los DataFrames
df_combinado = pd.concat(dataframes, ignore_index=True)

# Convertir el DataFrame combinado a JSON
json_data = df_combinado.to_json(orient='records')

# Guardar el JSON en un archivo
archivo_json = 'archivo_combinado.json'
with open(archivo_json, 'w') as f:
    f.write(json_data)

print(f"Archivo JSON combinado guardado como {archivo_json}")
