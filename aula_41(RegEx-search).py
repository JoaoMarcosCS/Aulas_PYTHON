import os
import re

os.system("cls")

texto="Curso de python, vamos ver se está funcionando"

pesq=input("Pesquisar: ")
res=re.search(pesq,texto)

if(res != None):
    i=res.start()
    f=res.end()
    tam=f-i
    print("Começa em: "+str(res.start())+"\n Termina em: "+str(res.end())+"\n Tamanho T: "+str(tam))
else:
    print(pesq+" não existe na string: "+texto)