import os
import json
import requests
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

TANGO_API_URL = os.getenv('TANGO_TIENDAS_API_URL')
TANGO_ACCESS_TOKEN = os.getenv('TANGO_TIENDAS_ACCESS_TOKEN')

def listar_skus_de_tango():
    last_sync_datetime = get_last_sync_datetime()
    print(last_sync_datetime)

    skus_habilitados = []
    skus_deshabilitados = []
    productos_con_composicion = {}

    with open('../disabled_products/skus_habilitados.txt', 'r') as file:
        skus = file.readlines()

    for sku in tqdm(skus, desc="Buscando SKUs y Composiciones", unit="sku"):
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

            if 'ProductComposition' in producto and producto['ProductComposition']:
                productos_con_composicion[sku] = {
                    'Componentes': [
                        {'SKU': comp['ComponentSKUCode'], 'Cantidad': comp['Quantity']}
                        for comp in producto['ProductComposition']
                    ]
                }

    with open('skus_habilitados.txt', 'w') as file:
        file.write('\n'.join(skus_habilitados))

    with open('skus_deshabilitados.txt', 'w') as file:
        file.write('\n'.join(skus_deshabilitados))

    with open('productos_con_composicion.json', 'w') as file:
        json.dump(productos_con_composicion, file, indent=4)

def get_last_sync_datetime():
    # Implementar lógica para obtener la última fecha de sincronización
    pass

listar_skus_de_tango()
