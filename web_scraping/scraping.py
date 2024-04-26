import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time

# Archivo de entrada con los enlaces de los productos
input_file = 'enlaces_productos.txt'

# Archivo de salida para guardar los datos encontrados
output_file = 'datos_productos.txt'

# Leer los enlaces de los productos desde el archivo
with open(input_file, 'r') as f:
    enlaces_productos = f.readlines()

# Función para mostrar una barra de progreso
def progress_bar(iterator, total=None):
    return tqdm(iterator, total=total, desc="Procesando enlaces", unit="enlace")

# Dividir los enlaces en lotes de 1000 para procesarlos por separado
batches = [enlaces_productos[i:i+1000] for i in range(0, len(enlaces_productos), 1000)]

# Abrir el archivo de salida en modo de escritura
with open(output_file, 'w') as f:
    for batch in batches:
        for enlace in progress_bar(batch):
            enlace = enlace.strip()

            # Realizar la solicitud HTTP
            response = requests.get(enlace)

            # Verificar si la solicitud fue exitosa
            if response.status_code == 200:
                # Parsear el contenido HTML
                soup = BeautifulSoup(response.text, 'html.parser')

                # Encontrar el SKU del producto
                sku_element = soup.find('span', class_='sku')
                if sku_element:
                    sku = sku_element.get_text().strip()

                    # Encontrar la URL de la imagen
                    figure_element = soup.find('figure', class_='woocommerce-product-gallery__image')
                    if figure_element:
                        href = figure_element.find('a')['href']
                        # print(f"SKU: {sku}, imagen: {href}")

                        # Guardar el SKU y la URL de la imagen en el archivo de salida
                        f.write(f"SKU: {sku}, imagen: {href}\n")
            else:
                print('Error al cargar la página:', response.status_code)

        # Agregar un tiempo de espera entre lotes para no sobrecargar el servidor
        time.sleep(5)  # Espera de 5 segundos entre lotes
