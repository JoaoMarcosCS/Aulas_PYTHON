from pytube import YouTube

link=input("link:")
path=input("Diretório onde o vídeo vai ser salvo: ")
yt=YouTube(link)

ys=yt.streams.get_highest_resolution()

print("Baixando")
ys.download(path)
print("Download completo")