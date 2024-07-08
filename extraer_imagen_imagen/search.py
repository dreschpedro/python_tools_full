from PIL import Image
import numpy as np

# Cargar la imagen
image_path = "imagen20.jpg"
image = Image.open(image_path)

# Convertir a array de numpy para facilitar la manipulación
image_array = np.array(image)

# Definir las coordenadas de los recortes (aquí tendrás que ajustar manualmente)
# Estas coordenadas son (left, upper, right, lower)
coords = [
    (208, 130, 2105, 1730),   # Coordenadas de la primera imagen
    (208, 1775, 2105, 3375)   # Coordenadas de la segunda imagen
]

# Recortar y guardar las imágenes individuales
for i, (left, upper, right, lower) in enumerate(coords):
    cropped_image = image.crop((left, upper, right, lower))
    cropped_image.save(f"extracted_image_{i + 1}.png")

print("Extracción completada.")
