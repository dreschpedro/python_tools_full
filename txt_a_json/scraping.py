# Importar las bibliotecas beautifulsoup y requests.
import requests
import bs4

# Hacer dos cadenas con la URL de búsqueda de Google predeterminada
# 'https://google.com/search?q=' y nuestra palabra clave de búsqueda personalizada.
# Concatenarlas.
text = "ALAS ANGEL BCO CH LWC"
url = 'https://google.com/search?q=' + text + '&tbm=isch'  # '&tbm=isch' es para buscar imágenes

print(url)

# Obtener los datos de la URL usando requests.get(url), almacenarlos en una variable, request_result.
request_result = requests.get(url)

# Crear sopa (BeautifulSoup) a partir de la solicitud obtenida.
soup = bs4.BeautifulSoup(request_result.text, "html.parser")

# Buscar todas las etiquetas <img> para obtener las URLs de las imágenes.
image_objects = soup.find_all('img')

# Imprimir el HTML completo del primer elemento de la lista de imágenes, si existe.
if image_objects:
    print(image_objects[2])
else:
    print("No se encontraron imágenes.")