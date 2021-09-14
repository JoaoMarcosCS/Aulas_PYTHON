import re
import os
os.system("cls")

texto="Curso de Python no Canal CFB curos, é muito bom!"

pesq=input("Pesquisar: ")

res=re.findall(pesq,texto)

qtd=len(res)#mostra a quantidade de strings na string texto

print(res)
print("Qtd: "+str(qtd))

for i in res:
    print(i)


