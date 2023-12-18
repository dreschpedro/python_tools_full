# Crea un entorno virtual:

echo "Creado el Entorno de desarrollo !"
python -m venv venv
echo "Creado el Entorno: venv"


# Activa el entorno virtual:
# En Windows:
# venv\Scripts\activate

# En macOS y Linux:
echo ""
echo ""
echo "Activando Entorno"
echo ""

source venv/Scripts/activate

echo ""
echo "Entorno Activado"
echo ""
echo ""

# Instalar las dependencias:
echo "Instalando las dependencias..."
echo ""

pip install -r requirements.txt

echo ""
echo "Instalados los paquetes"
echo ""
echo ""
