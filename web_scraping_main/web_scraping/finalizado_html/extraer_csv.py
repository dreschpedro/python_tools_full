import csv

# Ruta del archivo CSV
input_file = 'productos_sin_imagen.csv'
output_file = 'productos_resultado.csv'

# Lista para almacenar las líneas que cumplen con la condición
filtered_lines = []

# Leer el archivo CSV
with open(input_file, mode='r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if row[1].startswith('01'):
            filtered_lines.append(row)

# Escribir las líneas filtradas en un nuevo archivo CSV
with open(output_file, mode='w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(filtered_lines)

print(f"Líneas filtradas guardadas en {output_file}")
