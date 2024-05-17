from moviepy.editor import *

def extraer_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)

# Ruta del video de entrada
video_path = "./uber_clone.mp4"

# Ruta donde se guardará el archivo de audio extraído
audio_path = "./uber_clone.mp3"

# Extraer audio del video
extraer_audio(video_path, audio_path)

