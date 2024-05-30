import re
import json
from bs4 import BeautifulSoup

# Función para extraer códigos y URLs de imágenes del archivo HTML
def extraer_codigos_y_imagenes_html(ruta_archivo_html):
    with open(ruta_archivo_html, "r", encoding='utf-8') as f:
        contenido_html = f.read()

    soup = BeautifulSoup(contenido_html, 'html.parser')
    productos = soup.find_all(class_="product-grid fade")
    
    codigos_imagenes_html = []
    for producto in productos:
        texto_producto = producto.find("p").text
        match = re.search(r'CÓDIGO:\s*([\w\s]+)', texto_producto)
        if match:
            codigo = match.group(1).strip()
            # Buscar la URL de la imagen
            imagen_tag = producto.find("a", class_="fancyima")
            imagen_url = imagen_tag['href'] if imagen_tag else 'No image found'
            codigos_imagenes_html.append((codigo, imagen_url))
    return codigos_imagenes_html

# Función para extraer códigos del archivo JSON
def extraer_codigos_json(ruta_archivo_json):
    with open(ruta_archivo_json, "r", encoding='utf-8') as f:
        data = json.load(f)
    
    codigos_json = []
    for item in data:
        nombre = item.get("nombre", "")
        match = re.search(r'CODIGO\s([\w\s]+) PLASTICHOOK', nombre)
        if match:
            codigo = match.group(1).strip()
            item["codigo"] = codigo  # Añadir el código al dict para referencia futura
            codigos_json.append(item)
    return codigos_json

# Función para comparar códigos y encontrar coincidencias
def comparar_codigos(codigos_html, codigos_json):
    # Crear un diccionario para acceder rápidamente a la URL de la imagen por código
    dict_codigos_html = {codigo: imagen_url for codigo, imagen_url in codigos_html}
    
    # Lista para almacenar los productos coincidentes con las URLs de imágenes
    productos_con_imagenes = []

    # Encontrar las coincidencias y añadir la URL de la imagen al producto
    for item in codigos_json:
        codigo = item["codigo"]
        if codigo in dict_codigos_html:
            imagen_url = dict_codigos_html[codigo]
            item["image_url"] = f"http://www.plastichok.com.ar/{imagen_url}"
            del item["codigo"]  # Eliminar el campo "codigo" del diccionario
            productos_con_imagenes.append(item)
    
    return productos_con_imagenes

# Rutas de los archivos
ruta_archivo_html = "product_grids.html"
ruta_archivo_json = "PLASTICHOOK_productos.json"
ruta_archivo_salida_json = "productos_con_imagenes.json"

# Extraer códigos y URLs de imágenes del HTML
codigos_imagenes_html = extraer_codigos_y_imagenes_html(ruta_archivo_html)
# print("Códigos y URLs de imágenes extraídos del HTML:")
# for codigo, imagen in codigos_imagenes_html:
#     print("CÓDIGO:", codigo, "URL de la imagen:", imagen)

# Extraer códigos del JSON
codigos_json = extraer_codigos_json(ruta_archivo_json)
# print(f"\nCódigos extraídos del JSON: {ruta_archivo_json}")
# for item in codigos_json:
#     print("CÓDIGO:", item["codigo"], "ID:", item["id"], "SKU:", item["sku"])

# Comparar los códigos y encontrar coincidencias
productos_con_imagenes = comparar_codigos(codigos_imagenes_html, codigos_json)
# print("\nProductos coincidentes con URLs de imágenes:")
for producto in productos_con_imagenes:
    print("ID:", producto["id"], "SKU:", producto["sku"], "Image URL:", producto["image_url"])

# Guardar los productos coincidentes con URLs de imágenes en un nuevo archivo JSON
with open(ruta_archivo_salida_json, "w", encoding='utf-8') as f:
    json.dump(productos_con_imagenes, f, ensure_ascii=False, indent=4)
