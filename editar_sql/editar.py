# no agrega el inicio del parentesis al resultado


def agregar_comillas_from_sql(file_path, posiciones, output_file):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        result = []
        for line in lines:
            partes = line.strip().strip(')').strip('(').split(',')
            for pos in posiciones:
                if 0 <= pos < len(partes):
                    partes[pos] = "'" + partes[pos] + "'"
            result.append(','.join(partes))

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for dato in result:
            out_file.write(dato + '\n')

# Definir las posiciones donde quieres agregar las comillas
posiciones = [2, 3, 4, 5, 6, 7, 10]

# Nombre del archivo SQL de entrada y salida
input_file = 'tu_archivo.sql'
output_file = 'resultado.sql'

# Aplicar la función al archivo SQL
agregar_comillas_from_sql(input_file, posiciones, output_file)

print("Proceso completado. El archivo resultado.sql ha sido creado con éxito.")
