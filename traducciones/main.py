from translate import Translator
import polib
from tqdm import tqdm

# Ruta del archivo .po original
archivo_po_original = 'archivos/woocommerce-memberships-en_US.po'

# Ruta del archivo .po traducido
archivo_po_traducido = 'archivos/woocommerce-memberships-es_AR.po'

# Crear un objeto Translator
translator = Translator(to_lang='es')

# Cargar el archivo .po original
po_original = polib.pofile(archivo_po_original)

# Crear una barra de progreso
with tqdm(total=len(po_original)) as pbar:
    # Traducir cada entrada en el archivo original
    for entry in po_original:
        # Traducir el mensaje al español argentino
        translation = translator.translate(entry.msgid)
        entry.msgstr = translation
        # Actualizar la barra de progreso
        pbar.update(1)

# Guardar el archivo traducido
po_original.save(archivo_po_traducido)

print(f"Archivo .po traducido guardado en: {archivo_po_traducido}")
