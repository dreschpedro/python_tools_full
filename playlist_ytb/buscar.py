import mmap
from googlesearch import search

# Define el dominio que deseas buscar
dominio = "site:music.youtube.com"

# Nombre del archivo de salida
archivo_resultados = "resultados.txt"

# with open("lista_musica.txt", "r+") as myfile:
#     mm = mmap.mmap(myfile.fileno(), 0)
#     total_lines = 0

#     while mm.readline():
#         total_lines += 1

# print(f'***\ntiene {total_lines} lineas\n***')

archivo = open('lista_musica.txt', encoding='UTF-8')
archivo_leer = archivo.read()
archivo.close()

# Divide el contenido del archivo en líneas
lineas = archivo_leer.split('\n')

# Abre el archivo de resultados para escritura
with open(archivo_resultados, "w", encoding="utf-8") as resultados_file:
    # Realiza una búsqueda en Google para cada nombre de canción en el dominio de YouTube
    for cancion in lineas:
        if cancion.strip():  # Ignora líneas en blanco
            # Crea la consulta de búsqueda con el dominio específico
            google_query = f'{cancion} {dominio}'
            print(f'\nBuscando: {google_query}')
            
            iniciar_elemento = 0
            pausa_busqueda= 15
            cantidad_resultados= 1
            
            # Realiza la búsqueda y escribe los resultados en el archivo de resultados
            for resultado in search(google_query, start=iniciar_elemento, pause=pausa_busqueda, stop=cantidad_resultados):
                print(resultado)
                resultados_file.write(resultado + "\n")

print(f'\n##########\nResultados guardados en [{archivo_resultados}]')
