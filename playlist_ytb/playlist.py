from pytube.contrib.playlist import Playlist

playlist_url = input('URL de la playlist: ')
# Imprimir la URL para verificar que sea correcta
print("URL proporcionada:", playlist_url)

# Crear un objeto de la clase Playlist con la URL proporcionada
playlist = Playlist(playlist_url)

# Obtener la lista de videos de la playlist
videos = playlist.video_urls

# Guardar la lista de videos en un archivo
file_name = 'resultado.txt'
with open(file_name, 'w') as file:
    file.write("Canciones en la playlist:\n")
    for video_url in videos:
        file.write(video_url + '\n')

print(f"Se ha guardado la lista de canciones en el archivo '{file_name}'.")
