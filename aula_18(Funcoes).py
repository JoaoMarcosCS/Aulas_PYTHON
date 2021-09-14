import os

os.system("cls")

def somar(n1,n2,n3):
    print("resultado da soma: "+str(n1+n2+n3))

def soma(*n):
    r=0
    for i in n:
        r=r+i
    
    print("Soma total: "+str(r))

def texto(*n):# o n pode ser uma tupla, list, várias váriaveis, strings, matrizes de strings, dicionarios
   for i in n:
       print(i)


def carro(c="Vazio"):#caso a função seja chamada sem nenhum parametro, a variável c vai ter como valor vazio
    print(c)

def soma2(*n):
    r=0
    for i in n:
        r=r+i
    
    return r

somar(1,2,3)
texto("eeeee","aaaaa","rffrffr","ckeden","dekn","dkndei","dnebw")
soma(1,3,5,4,5,79,7,322,5421,7)
carro("HRV")

st=soma2(2,4,67,4,2,3,5,73,1,23,5,4)
print("Soma total(2):"+str(st)+" ou "+str(soma2(2,4,67,4,2,3,5,73,1,23,5,4)))


