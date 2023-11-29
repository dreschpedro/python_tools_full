from pytube import YouTube

url = input('URL del video o playlist: ')
YouTube(url).streams.first().download()
# yt = YouTube('https://www.youtube.com/shorts/YwrRBimFWq8')
# yt.streams
# filter(progressive=True, file_extension='mp4')
# order_by('resolution')
# desc()
# first()
# download()
