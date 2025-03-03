import os
import subprocess

def main():
    try:
        # Mostrar opciones iniciales
        print("Selecciona una opción:")
        print("1. Descargar un video")
        print("2. Descargar una lista de reproducción")
        opcion = input("Ingresa el número de tu elección (1 o 2): ")

        if opcion not in ["1", "2"]:
            print("Opción inválida. Saliendo del programa.")
            return

        # Pedir la URL según la opción seleccionada
        url = input("Ingresa la URL del video o lista de reproducción de YouTube: ")

        # Mostrar opciones de descarga
        print("\nSelecciona el tipo de descarga:")
        print("1. Video con audio")
        print("2. Solo audio")
        print("3. Solo video")
        tipo_descarga = input("Ingresa el número de tu elección (1, 2 o 3): ")

        if tipo_descarga not in ["1", "2", "3"]:
            print("Opción inválida. Saliendo del programa.")
            return

        # Crear un directorio para guardar las descargas
        output_dir = "descargas"
        os.makedirs(output_dir, exist_ok=True)

        # Construir el comando base
        command = ["yt-dlp", url, "-o", f"{output_dir}/%(title)s.%(ext)s"]

        # Configurar el formato de descarga
        if tipo_descarga == "1":
            command.extend(["-f", "bestvideo+bestaudio"])
        elif tipo_descarga == "2":
            command.extend(["-f", "bestaudio", "--extract-audio", "--audio-format", "mp3"])
        elif tipo_descarga == "3":
            command.extend(["-f", "bestvideo"])

        # Descargar el contenido
        print("\nDescargando...")
        subprocess.run(command)

        print(f"\n¡Descarga completada! Los archivos se guardaron en la carpeta '{output_dir}'.")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

if __name__ == "__main__":
    main()
