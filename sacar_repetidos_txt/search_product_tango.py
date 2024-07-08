import os
import json
import requests
import time
from tqdm import tqdm

# Configurar variables de entorno
tangoAPIURL = 'https://tiendas.axoft.com/api'
tangoAccessToken = 'd889efec-cea0-44c7-bfd6-3d2d72bace71_12829'

def get_tango_orders(sku):
    headers = {
        "accessToken": tangoAccessToken
    }

    url = f"{tangoAPIURL}/Aperture/Product?pageSize=5000&PageNumber=1&onlyKit=true&onlyEnabled=true&filter={sku}"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error en la petición: {response.status_code}")
        return None
    
    tango_response = response.json()

    if not tango_response or 'Data' not in tango_response or not tango_response['Data']:
        print(f"No data or error decoding JSON response for SKU: {sku}")
        return None

    product_compositions = []
    for product in tango_response['Data']:
        product_compositions.append({
            'SKU': product['SKUCode'],
            'ProductComposition': product['ProductComposition']
        })

    return product_compositions

def main():
    # Leer el archivo JSON de entrada
    try:
        with open('result.json', 'r') as file:
            input_data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error decodificando JSON: {e}")
        return

    results = []

    # Barra de progreso
    progress_bar = tqdm(input_data, desc="Procesando productos", unit="producto", dynamic_ncols=True)

    # Recorrer cada SKU en el archivo JSON de entrada y obtener la composición del producto
    for item in progress_bar:
        sku = item['SKU']
        time.sleep(2)  # Delay de 10 segundos por producto
        product_compositions = get_tango_orders(sku)
        
        if product_compositions:
            results.extend(product_compositions)
    
    # Escribir los resultados en un nuevo archivo JSON
    with open('product_compositions.json', 'w') as outfile:
        json.dump(results, outfile, indent=4)

    print("Proceso completado. Los resultados se han guardado en 'product_compositions.json'.")

if __name__ == "__main__":
    main()
