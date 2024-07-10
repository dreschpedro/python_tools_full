import os
import glob
from PIL import Image
import numpy as np

# Definir las coordenadas de los recortes (ajustar según sea necesario)
# Estas coordenadas son (left, upper, right, lower)
coords = [
    (415, 130, 2275, 1730),   # Coordenadas de la primera imagen
    (415, 1775, 2275, 3375)   # Coordenadas de la segunda imagen
]

# Obtener la lista de todas las imágenes en la carpeta
image_folder = "./images"  # Cambiar esto al nombre de tu carpeta
image_paths = glob.glob(os.path.join(image_folder, "*.jpg"))

# Procesar cada imagen
for image_path in image_paths:
    # Cargar la imagen
    image = Image.open(image_path)
    
    # Convertir a array de numpy para facilitar la manipulación (opcional)
    image_array = np.array(image)

    # Obtener el nombre base del archivo sin la extensión
    base_name = os.path.splitext(os.path.basename(image_path))[0]

    # Recortar y guardar las imágenes individuales
    for i, (left, upper, right, lower) in enumerate(coords):
        cropped_image = image.crop((left, upper, right, lower))
        cropped_image.save(os.path.join(image_folder, f"{base_name}_image{i + 1}.png"))

print("Extracción completada.")
