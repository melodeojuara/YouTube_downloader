### Baixar vídeo do YouTube ###

# Instalando biblioteca pytube.
import pytube
from pytube import YouTube

# Iniciando processo de download.
url_list = [input()]

for i in url_list:
  yt = YouTube(i) 
  video = yt.streams.get_lowest_resolution()
  video.download() 

  # Ajustando a duração do vídeo
  minutos = int(yt.length)//60
  if minutos > 59 :
    minutos = minutos - ((int(yt.length)//60)//60)*60
    horas = (int(yt.length)//60)//60
    segundos = int((int(yt.length)/60 - (int(yt.length)//60))*60)
    duracao = f"{horas}:{minutos}:{segundos}"
  else:
    horas = 0.
    minutos = int(yt.length)//60
    segundos = int((int(yt.length)/60 - (int(yt.length)//60))*60)
    duracao = f"{minutos}:{segundos}"
    
  # Dados do vídeo.
  print(f"Nome do vídeo: {yt.title}")
  print(f"Duração do vídeo: {duracao}")
  print(f"Tamanho do arquivo: {video._filesize // 1000000} Mb")
