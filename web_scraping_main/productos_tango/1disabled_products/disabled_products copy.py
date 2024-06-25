import os
import requests
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

TANGO_API_URL = os.getenv('TANGO_TIENDAS_API_URL')
TANGO_ACCESS_TOKEN = os.getenv('TANGO_TIENDAS_ACCESS_TOKEN')

def listar_skus_de_tango():
    last_sync_datetime = get_last_sync_datetime()
    print(last_sync_datetime)

    skus_habilitados = []
    skus_deshabilitados = []

    with open('skus.txt', 'r') as file:
        skus = file.readlines()

    for sku in tqdm(skus, desc="Buscando SKUs", unit="sku"):
        sku = sku.strip()  # Remove trailing newline
        response = requests.get(
            f"{TANGO_API_URL}/Aperture/Product",
            params={
                'pageSize': 1,
                'pageNumber': 1,
                'filter': sku,
                # 'updatedDate': last_sync_datetime
            },
            headers={'accessToken': TANGO_ACCESS_TOKEN}
        )
        data = response.json()

        if 'Data' in data and data['Data']:
            producto = data['Data'][0]
            if producto['Disabled']:
                skus_deshabilitados.append(sku)
            else:
                skus_habilitados.append(sku)
        else:
            print(f"No se encontró el SKU {sku} en la respuesta de Tango API.")

    with open('skus_habilitados.txt', 'w') as file:
        file.write('\n'.join(skus_habilitados))

    with open('skus_deshabilitados.txt', 'w') as file:
        file.write('\n'.join(skus_deshabilitados))

def get_last_sync_datetime():
    # Implementar lógica para obtener la última fecha de sincronización
    pass

listar_skus_de_tango()
