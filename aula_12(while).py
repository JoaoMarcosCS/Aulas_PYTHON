import os

os.system("cls")

carros=["1","2","3","4","5"]

i=0

tam=len(carros)

while i<tam:
    print(carros[i])
    i+=1
print("FIM")

numeros=[]

num=int(input("Entre com um numero(-1 para finalizar)"))
while num !=-1:
    numeros.append(num)
    num=int(input("Entre com um numero novamente:"))
os.system("cls")
for x in numeros:
    print(x)