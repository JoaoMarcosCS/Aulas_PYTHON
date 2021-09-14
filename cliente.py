from socket import *

#arquivo complementar de server.py, onde daqui que sairá as mensagens, mas o server.py precisa estar sendo executado[]


host=gethostname()# nome do host
port=55551  #porta onde o serviço será executado

print(f"HOST:{host}, PORT:{port}")

cliente=socket(AF_INET,SOCK_STREAM)#CRIAÇÃO DO SOCKET
cliente.connect((host,port))

while 1:
    msg=input("[client@root:~#]")
    cliente.send(msg.encode())




