import json

# Ruta del archivo JSON
archivo_json = 'goma.json'

# Cadena a buscar y reemplazar
cadena_buscar = 'GIBRE'
cadena_reemplazar = 'GLITTER'

# Leer el archivo JSON
with open(archivo_json, 'r') as file:
    data = json.load(file)

# Recorrer cada objeto en la lista
for obj in data:
    # Reemplazar la cadena en el nombre
    obj['nombre'] = obj['nombre'].replace(cadena_buscar, cadena_reemplazar)

# Escribir el archivo JSON modificado
with open(archivo_json, 'w') as file:
    json.dump(data, file, indent=2)
