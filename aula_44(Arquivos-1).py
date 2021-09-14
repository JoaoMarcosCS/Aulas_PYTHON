import os

os.system("cls")



f=open("C:/Users/João Marcos/Documents/João Marcos - Cotec/Python/testepy.txt","wt")

"""
r - read - Leitura
a - append - Adiciona um conteudo sem apagar o já existente
w - write - Escrita, apaga o conteudo
x - creat - cria um arquivo

t - modo texto
b - modo binário

"""
f.write("\nOlaaa\n")


txt=input("Texto: ")
f.write(txt+"\n")

f.close()

f=open("C:/Users/João Marcos/Documents/João Marcos - Cotec/Python/testepy.txt","rt")

print("-------LETTURA DO ARQUIVO---------")
#print(f.read())#faz a leitura do conteudo todo
for i in f:
    print(i)
    #linha=re.sub("\s",".",f.readline())#substitui os espaços por . da string retornada
    linha=i
    print(linha)

f.close()