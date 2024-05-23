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

def download_image(url, folder_name, num):
    # Escribir imagen en un archivo
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder_name, str(num) + ".jpg"), 'wb') as file:
            file.write(response.content)

# Leer el archivo JSON
with open('velas.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extraer los nombres de los productos
queries = [item['nombre'] for item in data]

# Configuración de opciones de Chrome
chromePath = r'C:\Users\taller 2\Documents\chromedriver-win64\chromedriver.exe'
chrome_options = Options()
chrome_service = Service(chromePath)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

for idx, query in enumerate(queries, start=1):
    search_URL = f"https://www.google.com/search?q={query}&source=lnms&tbm=isch"
    driver.get(search_URL)

    input("Waiting...")

    # Desplazarse hasta arriba
    driver.execute_script("window.scrollTo(0, 0);")

    page_html = driver.page_source
    pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
    first_container = pageSoup.find('div', {'jscontroller': "Um3BXb"})

    if first_container:
        print("Contenedor encontrado, procesando...")

        try:
            # XPath de la imagen de vista previa
            previewImageXPath = "(//div[@jscontroller='Um3BXb']//img)[1]"
            previewImageElement = driver.find_element("xpath", previewImageXPath)
            previewImageURL = previewImageElement.get_attribute("src")

            # Hacer clic en el contenedor
            containerXPath = "(//div[@jscontroller='Um3BXb'])[1]"
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
                download_image(imageURL, folder_name, idx)
                print(f"Imagen descargada. URL: {imageURL}")
            except Exception as e:
                print(f"No se pudo descargar la imagen. Error: {e}")
        except Exception as e:
            print(f"No se pudo procesar el contenedor. Error: {e}")
    else:
        print("No se encontró ningún contenedor.")

driver.quit()
