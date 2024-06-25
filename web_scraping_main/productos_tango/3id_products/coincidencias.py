# Leer el archivo sku.txt y almacenar los SKUs en un conjunto
skus = set()
with open('sku.txt', 'r') as f:
    for line in f:
        skus.add(line.strip())

# Leer el archivo id_sku.txt y buscar coincidencias de SKU
coincidencias = []
with open('id_sku.txt', 'r') as f:
    for line in f:
        parts = line.strip().split(',')
        if len(parts) == 2:
            if parts[1] in skus:
                coincidencias.append((parts[1], parts[0]))

# Escribir las coincidencias en un nuevo archivo
with open('coincidencias.txt', 'w') as f:
    for sku, id_sku in coincidencias:
        f.write(f'{sku},{id_sku}\n')
