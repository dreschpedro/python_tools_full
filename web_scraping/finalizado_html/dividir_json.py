import json

def dividir_json_por_categoria(archivo_entrada, prefijo_salida):
    with open(archivo_entrada, 'r') as f:
        productos = json.load(f)
    
    productos_por_categoria = {}
    
    # Agrupar productos por los primeros 2 dígitos del SKU
    for producto in productos:
        categoria_id = str(producto['sku'])[:2]
        if categoria_id not in productos_por_categoria:
            productos_por_categoria[categoria_id] = []
        productos_por_categoria[categoria_id].append(producto)
    
    # Guardar cada categoría en un archivo separado
    for categoria_id, productos in productos_por_categoria.items():
        archivo_salida = f"{prefijo_salida}_categoria_{categoria_id}.json"
        with open(archivo_salida, 'w') as f:
            json.dump(productos, f, indent=4)

# Uso del método
dividir_json_por_categoria('json_combinado_completo.json', 'productos')
