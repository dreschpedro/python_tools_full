import json

# Lee el JSON desde un archivo
with open('imagen_data111111.json') as file:
    json_data = json.load(file)

# Itera sobre cada elemento del JSON y modifica el SKU
for producto in json_data:
    sku = str(producto["sku"])  # Convierte el SKU a cadena
    sku_con_ceros = sku.zfill(10)  # Agrega ceros al principio para hacerlo de 10 dígitos
    producto["sku"] = sku_con_ceros

# Escribe el JSON modificado en un nuevo archivo
with open('datos_modificados.json', 'w') as file:
    json.dump(json_data, file, indent=2)

print("Se ha creado el archivo 'datos_modificados.json' con los SKUs actualizados.")
