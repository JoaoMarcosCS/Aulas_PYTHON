import os
import re

os.system("cls")

caminho="C:/Users/João Marcos/Documents/João Marcos - Cotec/Python/testepy.txt"

if os.path.exists(caminho):
    print("Arquivo existente")
    os.remove(caminho)
    if os.path.exists(caminho):
        print("Arquivo não removido")
    else:
        print("Arquivo removido")
else:
    f=open(caminho,"x")
