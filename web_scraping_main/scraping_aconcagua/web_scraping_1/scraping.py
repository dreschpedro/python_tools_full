import bs4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

# Función para guardar datos en JSON
def save_image_data(data, filename):
    try:
        with open(filename, 'r') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []
    
    existing_data.append(data)
    
    with open(filename, 'w') as file:
        json.dump(existing_data, file, indent=4)

# Leer datos del archivo JSON
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extraer nombres de productos y SKUs
products = [{'nombre': item['nombre'], 'sku': item['sku']} for item in data]

# Configuración de Selenium y ChromeDriver
chromePath = r'C:\Users\taller\Documents\chromedriver-win64\chromedriver.exe'
chrome_options = Options()
chrome_service = Service(chromePath)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Iterar sobre cada producto para buscar imágenes
for product in products:
    query = product['nombre']
    sku = product['sku']
    search_URL = f"https://www.google.com/search?q={query}&source=lnms&tbm=isch"
    driver.get(search_URL)
    
    # Esperar a que la página se cargue completamente
    print(f"Buscando imágenes para: {query}")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img')))

    # Obtener el HTML de la página actual
    page_html = driver.page_source
    pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')

    # Encontrar todos los contenedores de imágenes
    containers = driver.find_elements(By.CSS_SELECTOR, 'div[jscontroller="Um3BXb"]')
    
    # Imprimir la cantidad de contenedores encontrados
    print(f"Cantidad de contenedores encontrados para {query}: {len(containers)}")
    
    if containers:
        print(f"Contenedores encontrados para {query}, procesando...")

        # Limitar a las imágenes de la 1 a la 20 (20 imágenes)
        for i, container in enumerate(containers[0:10]):
            try:
                # Hacer clic en el contenedor de la imagen
                container.click()

                # Esperar a que la imagen completa se cargue
                print("Esperar a que la imagen completa se cargue")
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'img.sFlh5c.FyHeAf.iPVvYb'))
                )

                # Pausa después de hacer clic en la imagen
                time.sleep(5)  # Espera adicional después de hacer clic en la imagen

                # Encontrar la URL de la imagen
                print("Encontrar la URL de la imagen")
                # image_element = driver.find_element(By.CSS_SELECTOR, 'img.sFlh5c.pT0Scc.iPVvYb')
                image_element = driver.find_element(By.CSS_SELECTOR, 'img.sFlh5c.FyHeAf.iPVvYb')
                image_url = image_element.get_attribute('src')
                print(f"URL de imagen encontrada ({i + 1}): {image_url}")

                # Guardar la URL de la imagen en image_data.json
                image_data = {'sku': sku, 'image_url': image_url}
                save_image_data(image_data, 'image_data.json')

                # Cerrar la vista de la imagen
                container.click()

            except Exception as e:
                print(f"No se pudo procesar el contenedor {i + 1}. Error: {e}")

        # Pausa adicional antes de procesar el siguiente producto
        print(f"Finalizado procesamiento para {query}, esperando antes de continuar...")
        time.sleep(5)  # Ajusta este tiempo si es necesario

    else:
        print(f"No se encontraron contenedores de imágenes para {query}.")

# Cerrar el navegador al finalizar
driver.quit()
