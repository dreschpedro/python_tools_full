import json
import hashlib

# Lista de colores predefinidos
colores = ["#86E3CE", "#D0E6A5", "#FFDD94", "#FA897B", "#CCABD8", "#CBE54E"]

def generate_color(sku):
    hash_object = hashlib.md5(sku.encode())
    hash_int = int(hash_object.hexdigest(), 16)
    r = (hash_int & 0xFF0000) >> 16
    g = (hash_int & 0x00FF00) >> 8
    b = hash_int & 0x0000FF
    color = f"#{r:02x}{g:02x}{b:02x}"
    background_color = f"{color}33"  # Añadir opacidad al color de fondo
    return color, background_color


# Carga de productos y categorías
with open('result.json', 'r', encoding='utf-8') as file:
    json_combinado = json.load(file)

with open('categorias.json', 'r', encoding='utf-8') as file:
    categorias = json.load(file)

# Separar productos por categoría y subcategoría
productos_por_categoria_subcategoria = {}
for producto in json_combinado:
    sku = str(producto['sku'])
    categoria_id = sku[:2]
    subcategoria_id = sku[2:4]
    if categoria_id not in productos_por_categoria_subcategoria:
        productos_por_categoria_subcategoria[categoria_id] = {}
    if subcategoria_id not in productos_por_categoria_subcategoria[categoria_id]:
        productos_por_categoria_subcategoria[categoria_id][subcategoria_id] = []
    productos_por_categoria_subcategoria[categoria_id][subcategoria_id].append(producto)

# Generar contenido HTML
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Productos</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #333;
            color: white;
            padding: 10px 0;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        nav ul {
            list-style-type: none;
            padding: 0;
            margin: 0;
            display: flex;
            justify-content: center;
        }
        nav ul li {
            margin: 0 15px;
        }
        nav ul li select {
            color: black;
            background-color: white;
            padding: 10px;
            border: 2px solid #ccc;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        nav ul li select:hover {
            border-color: #888;
        }
        .productos-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            padding: 20px;
            padding-top: 60px;
        }
        .producto {
            padding: 10px;
            max-width: 200px;
            position: relative;
            cursor: pointer;
        }
        .producto img {
            max-width: 100%;
            height: auto;
        }
        .producto-checkbox {
            position: absolute;
            bottom: 10px;
            left: 80%;
            transform: translateX(-50%);
            width: 30px;
            height: 30px;
            opacity: 0;
            cursor: pointer;
        }
        .producto-selected .producto-checkbox {
            opacity: 1;
        }
        .producto-order {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: #c9ab34;
            color: white;
            padding: 5px;
            border-radius: 5px;
            font-size: 18px;
            display: none;
        }
        .producto-selected .producto-order {
            display: block;
        }
        section {
            display: none;
        }
        section.active {
            display: block;
        }
        button {
            background-color: green;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            margin-right: 20px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: darkgreen;
        }
        #buscador {
            padding: 8px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            width: 200px;
            box-sizing: border-box;
        }
        @media only screen and (max-width: 600px) {
            header {
                flex-direction: column;
                align-items: stretch;
            }
            nav {
                margin-bottom: 10px;
            }
            #buscador {
                width: 100%;
            }
            button {
                margin-top: 10px;
                width: 100%;
            }
        }
    </style>
    <script>
        let selectionOrder = {};

        function showCategory(categoryId) {
            const sections = document.querySelectorAll("section");
            sections.forEach((section) => {
                section.classList.remove("active");
            });
            const activeSection = document.getElementById(categoryId);
            if (activeSection) {
                activeSection.classList.add("active");
            }
        }

        function handleProductoClick(event) {
            const producto = event.currentTarget;
            const checkbox = producto.querySelector(".producto-checkbox");
            checkbox.checked = !checkbox.checked;
            producto.classList.toggle("producto-selected");

            const sku = producto.querySelector('p').textContent.split(' ')[1];
            const imageUrl = producto.querySelector('img').src;

            if (!selectionOrder[sku]) {
                selectionOrder[sku] = [];
            }

            if (producto.classList.contains('producto-selected')) {
                selectionOrder[sku].push(imageUrl);
            } else {
                const index = selectionOrder[sku].indexOf(imageUrl);
                if (index > -1) {
                    selectionOrder[sku].splice(index, 1);
                }
            }

            updateSelectionOrderDisplay(sku);
        }

        function updateSelectionOrderDisplay(sku) {
            const productos = document.querySelectorAll(`.sku-${sku}`);
            productos.forEach((producto) => {
                const orderElement = producto.querySelector('.producto-order');
                orderElement.textContent = selectionOrder[sku].indexOf(producto.querySelector('img').src) + 1;
            });
        }

        function filtrarProductos() {
            const filtro = document.getElementById('buscador').value.toLowerCase();
            const productos = document.querySelectorAll('.producto');

            productos.forEach(producto => {
                const nombre = producto.querySelector('h3').textContent.toLowerCase();
                const sku = producto.querySelector('p').textContent.toLowerCase();

                if (nombre.includes(filtro) || sku.includes(filtro)) {
                    producto.style.display = 'block';
                } else {
                    producto.style.display = 'none';
                }
            });
        }

        function procesarProductos() {
            const productosSeleccionados = [];
            for (const sku in selectionOrder) {
                if (selectionOrder[sku].length > 0) {
                    const producto = document.querySelector(`.sku-${sku}`);
                    const nombre = producto.querySelector('h3').textContent;
                    productosSeleccionados.push({
                        sku: sku,
                        nombre: nombre,
                        images: selectionOrder[sku]
                    });
                }
            }

            if (productosSeleccionados.length === 0) {
                alert('No hay productos seleccionados.');
                return;
            }

            const confirmacion = confirm(`¿Deseas procesar ${productosSeleccionados.length} productos seleccionados?`);
            if (confirmacion) {
                const jsonProductos = JSON.stringify(productosSeleccionados, null, 2);
                const blob = new Blob([jsonProductos], { type: 'application/json' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'productos_seleccionados.json';
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
            }
        }

        document.addEventListener('DOMContentLoaded', function() {
            const select = document.querySelector('select');
            if (select) {
                const firstOption = select.querySelector('option:nth-child(2)'); // Omitir la primera opción
                if (firstOption) {
                    firstOption.selected = true;
                    showCategory(firstOption.value);
                }
            }
        });
    </script>

</head>
<body>
<header>
    <nav>
        <ul>
            <li>
                <select onchange="showCategory(this.value)">
                    <option value="">Seleccione una categoría</option>
"""

# Añadir opciones de categoría y subcategoría
for categoria_id, categoria in categorias.items():
    if categoria_id in productos_por_categoria_subcategoria:
        for subcategoria_id, subcategoria in categoria['subcategories'].items():
            if subcategoria_id in productos_por_categoria_subcategoria[categoria_id]:
                html_content += f"<option value='{categoria_id}{subcategoria_id}'>{categoria['name']} - {subcategoria['name']}</option>\n"

html_content += """
                </select>
            </li>
        </ul>
    </nav>
    <input type="text" id="buscador" placeholder="Buscar por nombre o SKU..." oninput="filtrarProductos()">
    <button onclick="procesarProductos()">Procesar</button>
</header>

<div class="productos-container">
"""

# Generar estilos para cada producto
styles = ""
for producto in json_combinado:
    sku = str(producto['sku'])
    border_color, background_color = generate_color(sku)
    styles += f".sku-{sku} {{ border: 4px solid {border_color}; background-color: {background_color}; }}\n"

html_content += f"<style>\n{styles}</style>\n"

# Crear secciones para cada subcategoría
for categoria_id, subcategorias in productos_por_categoria_subcategoria.items():
    for subcategoria_id, productos in subcategorias.items():
        categoria_nombre = categorias[categoria_id]['name']
        subcategoria_nombre = categorias[categoria_id]['subcategories'][subcategoria_id]['name']

        html_content += f"<section id='{categoria_id}{subcategoria_id}'>\n"
        html_content += f"<h2>{categoria_nombre} - {subcategoria_nombre}</h2>\n"
        html_content += "<div class='productos-container'>\n"
        for producto in productos:
            sku = str(producto['sku'])
            html_content += f"<div class='producto sku-{sku}' onclick='handleProductoClick(event)'>\n"
            html_content += f"<img src='{producto['image_url']}' alt='Imagen del producto'>\n"
            html_content += f"<h3>{producto['nombre']}</h3>\n"
            html_content += f"<p>SKU: {producto['sku']}</p>\n"
            html_content += f"<input type='checkbox' class='producto-checkbox'>\n"
            html_content += f"<div class='producto-order'></div>\n"  # Arreglado: comillas dobles a comillas simples
            html_content += f"</div>\n"
        html_content += "</div>\n</section>\n"

html_content += """
</div>
</body>
</html>
"""


# Guardar el contenido HTML en un archivo
with open('productos.html', 'w', encoding='utf-8') as file:
    file.write(html_content)


print("Se ha creado el archivo productos.html con la navegación por categorías y productos correspondientes.")
