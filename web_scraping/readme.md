# Procesador de Enlaces de Productos

Este script de Python procesa una lista de enlaces de productos para extraer información útil, como el SKU y la URL de la imagen de cada producto. Está diseñado para manejar grandes cantidades de enlaces y evitar problemas de sobrecarga del servidor.

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/procesador-enlaces-productos.git
   ```

2. Instala las dependencias necesarias:

   ```bash
   pip install requests beautifulsoup4 tqdm
   ```

## Uso

1. Coloca los enlaces de los productos en un archivo de texto llamado `enlaces_productos.txt`, uno por línea.
2. Ejecuta el script `scraping.py`:

   ```bash
   python procesar_enlaces_productos.py
   ```

3. El script procesará los enlaces y guardará la información en un archivo de texto llamado `datos_productos.txt`.

## Funcionamiento

El script realiza lo siguiente:

1. Lee los enlaces de los productos desde `enlaces_productos.txt`.
2. Divide los enlaces en lotes de 1000 para procesarlos por separado.
3. Para cada enlace, realiza una solicitud HTTP para obtener el contenido HTML de la página.
4. Extrae el SKU y la URL de la imagen de cada producto.
5. Guarda el SKU y la URL de la imagen en `datos_productos.txt`.

El script incluye medidas para evitar problemas de sobrecarga del servidor, como la división de enlaces en lotes y la introducción de retardos entre solicitudes.

## Contribución

Si encuentras algún problema o tienes alguna sugerencia de mejora, por favor, abre un problema en el repositorio o envía una solicitud de extracción con tus cambios.
