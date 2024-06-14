import pandas as pd
import json


# nombre_archivo = input('Nombre del archivo (sin extensión): ')
nombre_archivo = 'prodcutos_reposteria_sin_imagen'
nombre_hoja = input('Nombre de la hoja del excel: ')

# Read excel document
excel_data_df = pd.read_excel(
    f'{nombre_archivo}.xlsx', sheet_name=nombre_hoja)

# Convert excel to string
# (define orientation of document in this case from up to down)
thisisjson = excel_data_df.to_json(orient='records')

# Print out the result
print('\nExcel Sheet to JSON:\n\n', thisisjson)

# Make the string into a list to be able to input in to a JSON-file
thisisjson_dict = json.loads(thisisjson)

# Define file to write to and 'w' for write option -> json.dump()
# defining the list to write from and file to write to
with open('data.json', 'w', encoding='UTF-8') as json_file:
    json.dump(thisisjson_dict, json_file)
