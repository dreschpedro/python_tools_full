import json

# Cargar el JSON con las URLs de las imágenes
with open('resultado.json', 'r') as file:
    json_imagenes = json.load(file)

# Cargar el JSON con los nombres de los productos
with open('data.json', 'r') as file:
    json_nombres = json.load(file)

# Combinar los dos JSON en uno solo
json_combinado = []

# Crear un diccionario para mapear SKU a nombres
sku_to_nombre = {entry["sku"]: entry["nombre"] for entry in json_nombres}

# Iterar sobre las entradas del JSON de imágenes
for imagen in json_imagenes:
    sku = imagen["sku"]
    if sku in sku_to_nombre:
        nombre = sku_to_nombre[sku]
        id_ = imagen["id"]
        image_url = imagen["image_url"]
        # Añadir el nombre, id, sku y la url de la imagen al JSON combinado
        json_combinado.append({"id": id_, "nombre": nombre, "sku": sku, "image_url": image_url})

# Guardar el resultado en un nuevo archivo JSON
with open('json_combinado.json', 'w') as file:
    json.dump(json_combinado, file, indent=4)

print("Se ha creado el archivo json_combinado.json con los datos combinados.")
