from socket import *

host=gethostname()# nome do host
port=55551  #porta onde o serviço será executado

print(f"HOST:{host}, PORT:{port}")

serv=socket(AF_INET,SOCK_STREAM)#CRIAÇÃO DO SOCKET

serv.bind((host,port))#necessário para "executar" tudo 

serv.listen(5)#determina quantas pessoas podem acessar os servidores

#----receber as mensagens------
#a pessoa deve utilizar os endreços host e port para enviarem as mensagens para o meu computador

while 1:
    con,adr=serv.accept()#recebe os dados criptografados, meio que "aceita" as mensagens enviadas
    while 1:
        msg=con.recv(1024)#aqui a mesnagem pode ser passada à uma váriavel
        msg=msg.decode()#descriptografa as mensagens
        print(msg)
