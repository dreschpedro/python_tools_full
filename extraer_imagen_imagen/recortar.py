import os
import glob
from PIL import Image
import numpy as np

# Definir las coordenadas de los recortes (ajustar según sea necesario)
# Estas coordenadas son (left, upper, right, lower)
# coords = [
#     (0, 630, 1400, 1730),   # Coordenadas de la primera imagen
#     (0, 2400, 1400, 3405)   # Coordenadas de la segunda imagen
# ]

coords = [
    (110, 465, 750, 1010),   #1 imagen
    (110, 1455, 750, 2000),   #2 imagen
    (110, 2530, 750, 3075),   #3 imagen

    (930, 465, 1570, 1010),   #4 imagen
    (930, 1455, 1570, 2000),   #5 imagen
    (930, 2530, 1570, 3075),   #6 imagen

    (1750, 465, 2390, 1010),   #7 imagen
    (1750, 1455, 2390, 2000),  #8 imagen
    (1750, 2530, 2390, 3075),  #9 imagen
]

# +---------+---------+---------+
# |         |         |         |
# |   I1    |   I4    |   I7    |
# |         |         |         |
# +---------+---------+---------+
# |         |         |         |
# |   I2    |   I5    |   I8    |
# |         |         |         |
# +---------+---------+---------+
# |         |         |         |
# |   I3    |   I6    |   I9    |
# |         |         |         |
# +---------+---------+---------+



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
