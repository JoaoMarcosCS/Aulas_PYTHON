import pytube

link="https://youtu.be/-eIStUWXh-0"

youtube=pytube.YouTube(link)
stream=youtube.streams.first()
stream.download()