def remove_duplicates(input_file, output_file):
    # Leer las líneas del archivo de entrada
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Usar un conjunto para almacenar líneas únicas
    unique_lines = set(lines)

    # Escribir las líneas únicas en el archivo de salida
    with open(output_file, 'w') as file:
        for line in unique_lines:
            file.write(line)

# Ruta del archivo de entrada y de salida
input_file = 'archivo.txt'
output_file = 'output.txt'

# Llamar a la función para eliminar duplicados
remove_duplicates(input_file, output_file)
