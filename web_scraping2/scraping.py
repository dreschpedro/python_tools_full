import bs4
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import json

# Crear un directorio para guardar las imágenes
folder_name = 'images'
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)

# Solicitar el número máximo de imágenes a descargar por búsqueda
while True:
    try:
        max_images = int(input('Cantidad de imágenes a descargar: '))
        if max_images > 0:
            max_images = max_images + 1
            break
        else:
            print("Por favor, introduce un número mayor a 0.")
    except ValueError:
        print("Por favor, introduce un número válido.")

def download_image(url, folder_name, sku, index):
    # Escribir imagen en un archivo
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder_name, f"{sku}_{index}.jpg"), 'wb') as file:
            file.write(response.content)

def save_image_data(data, filename):
    # Intenta cargar los datos existentes
    try:
        with open(filename, 'r') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []
    
    # Agrega el nuevo dato a la lista de datos existentes
    existing_data.append(data)
    
    # Guarda todos los datos juntos
    with open(filename, 'w') as file:
        json.dump(existing_data, file, indent=4)

# Leer el archivo JSON
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extraer los nombres de los productos y los SKUs
products = [{'nombre': item['nombre'], 'sku': item['sku']} for item in data]

# Configuración de opciones de Chrome
chromePath = r'C:\Users\taller 2\Documents\chromedriver-win64\chromedriver.exe'
chrome_options = Options()
chrome_service = Service(chromePath)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

for product in products:
    query = product['nombre']
    sku = product['sku']
    search_URL = f"https://www.google.com/search?q={query}&source=lnms&tbm=isch"
    driver.get(search_URL)
    
    # Esperar un tiempo para que la página se cargue completamente
    time.sleep(5)

    # Desplazarse hasta arriba
    driver.execute_script("window.scrollTo(0, 0);")

    page_html = driver.page_source
    pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
    containers = pageSoup.find_all('div', {'jscontroller': "Um3BXb"}, limit=max_images)

    if containers:
        print("Contenedores encontrados, procesando...")

        for i, container in enumerate(containers):
            try:
                # XPath de la imagen de vista previa
                previewImageXPath = f"(//div[@jscontroller='Um3BXb']//img)[{i + 1}]"
                previewImageElement = driver.find_element("xpath", previewImageXPath)
                previewImageURL = previewImageElement.get_attribute("src")

                # Hacer clic en el contenedor
                containerXPath = f"(//div[@jscontroller='Um3BXb'])[{i + 1}]"
                driver.find_element("xpath", containerXPath).click()

                # Esperar a que la imagen completa se cargue
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//a[contains(@class,'jlTjKd')]/img[@class='sFlh5c pT0Scc iPVvYb']"))
                )

                # Obtener la URL de la imagen completa
                imageElement = driver.find_element("xpath", "//a[contains(@class,'jlTjKd')]/img[@class='sFlh5c pT0Scc iPVvYb']")
                imageURL = imageElement.get_attribute('src')

                # Descargar imagen
                try:
                    # download_image(imageURL, folder_name, sku, i + 1)
                    # print(f"Imagen descargada. URL: {imageURL}")
                    # Guardar la URL de la imagen, la ruta de la imagen y el SKU en otro archivo JSON
                    time.sleep(10)
                    
                    image_data = {'sku': sku, 'image_url': imageURL}
                    save_image_data(image_data, 'image_data.json')
                except Exception as e:
                    print(f"No se pudo descargar la imagen. Error: {e}")
            except Exception as e:
                print(f"No se pudo procesar el contenedor {i + 1}. Error: {e}")
    else:
        print("No se encontró ningún contenedor.")

driver.quit()
