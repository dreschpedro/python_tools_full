from PIL import Image
import numpy as np

# Cargar la imagen
image_path = "imagen.jpg"
image = Image.open(image_path)

# Convertir a array de numpy para facilitar la manipulación
image_array = np.array(image)

# Definir las coordenadas de los recortes (aquí tendrás que ajustar manualmente)
# Estas coordenadas son (left, upper, right, lower)

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


# Recortar y guardar las imágenes individuales
for i, (left, upper, right, lower) in enumerate(coords):
    cropped_image = image.crop((left, upper, right, lower))
    cropped_image.save(f"extracted_image_{i + 1}.png")

print("Extracción completada.")
