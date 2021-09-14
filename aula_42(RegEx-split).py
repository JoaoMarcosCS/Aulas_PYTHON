import os
import re

os.system("cls")

texto="Curos de py lá no canal CFB curso"

res=re.split("\s",texto)#Aqui eu poderia por somente o espaço em branco

print(res)
print(res[2])

for i in res:
    print(i)

res=re.split("s",texto)

for i in res:
    print(i)