import requests
import re
import json
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
}

params = {
    "q": "michael jordan",  # search query
    "tbm": "isch",          # image results
    "hl": "sp",             # language of the search
    "gl": "ar",             # country where search comes from
}

html = requests.get("https://google.com/search", params=params, headers=headers, timeout=30)
soup = BeautifulSoup(html.text, "lxml")

google_images = []
all_script_tags = soup.select("script")

# Debug: imprimir la cantidad de scripts encontrados
print(f"Total script tags found: {len(all_script_tags)}")

# Regex para encontrar los datos de las imágenes en los scripts
matched_images_data = "".join(re.findall(r"AF_initDataCallback\(([^<]+)\);", str(all_script_tags)))

# Debug: imprimir los datos encontrados por la regex
print(f"Matched images data: {matched_images_data[:500]}")  # Limitar la salida a los primeros 500 caracteres

# Verificar si se encontraron datos antes de intentar cargarlos como JSON
if not matched_images_data:
    print("No image data found. Exiting...")
    exit()

# Limpieza de datos para que sea un JSON válido
matched_images_data_fix = re.sub(r"\\x22", "\"", matched_images_data)

# Debug: imprimir la cadena de datos fijada
print(f"Fixed matched images data: {matched_images_data_fix[:500]}")  # Limitar la salida a los primeros 500 caracteres

# Extrae JSON de los datos
try:
    matched_images_data_json = json.loads(matched_images_data_fix)
except json.JSONDecodeError as e:
    print(f"JSON decode error: {e}")
    exit()

# Busca los datos de las imágenes en el JSON
matched_google_image_data = re.findall(r'\"b-GRID_STATE0\"(.*)sideChannel:\s?{}}', str(matched_images_data_json))

# Extrae las URLs de las miniaturas de las imágenes
matched_google_images_thumbnails = ", ".join(
    re.findall(r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]', str(matched_google_image_data))
).split(", ")

# Decodifica las URLs de las miniaturas
thumbnails = [
    bytes(bytes(thumbnail, "ascii").decode("unicode-escape"), "ascii").decode("unicode-escape")
    for thumbnail in matched_google_images_thumbnails
]

# Elimina las miniaturas previamente encontradas para encontrar las imágenes de alta resolución
removed_matched_google_images_thumbnails = re.sub(
    r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]', "", str(matched_google_image_data)
)

# Busca las URLs de las imágenes de alta resolución
matched_google_full_resolution_images = re.findall(
    r"(?:'|,),\[\"(https:|http.*?)\",\d+,\d+\]", removed_matched_google_images_thumbnails
)

# Decodifica las URLs de las imágenes de alta resolución
full_res_images = [
    bytes(bytes(img, "ascii").decode("unicode-escape"), "ascii").decode("unicode-escape")
    for img in matched_google_full_resolution_images
]

# Extrae los metadatos y construye el array de resultados
for index, (metadata, thumbnail, original) in enumerate(
        zip(soup.select('.isv-r.PNCib.MSM1fd.BUooTd'), thumbnails, full_res_images), start=1):
    google_images.append({
        "title": metadata.select_one(".VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb")["title"],
        "link": metadata.select_one(".VFACy.kGQAp.sMi44c.lNHeqe.WGvvNb")["href"],
        "source": metadata.select_one(".fxgdke").text,
        "thumbnail": thumbnail,
        "original": original
    })

print(json.dumps(google_images, indent=2, ensure_ascii=False))
