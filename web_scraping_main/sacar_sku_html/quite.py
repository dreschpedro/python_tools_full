from bs4 import BeautifulSoup
import json

# Leer el contenido del archivo HTML
with open('repetidos.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parsear el contenido HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extraer los datos de los productos y eliminar duplicados
productos = {}
for product in soup.find_all('div', class_='producto'):
    nombre = product.find('h3').text
    sku = product.find('p').text.split(': ')[1]
    if sku not in productos:
        productos[sku] = {"nombre": nombre, "sku": sku}

# Convertir el diccionario a una lista
productos_unicos = list(productos.values())

# Guardar los datos en un archivo JSON
with open('productos.json', 'w', encoding='utf-8') as file:
    json.dump(productos_unicos, file, ensure_ascii=False, indent=4)

print("Datos extraídos y guardados en productos.json")
