import os
import re

os.system("cls")


texto="Curos de py, lá no canal CFB curso"

res=re.sub("\s","-",texto)#Aqui eu poderia por somente o espaço em branco

print(res)

res=re.sub(",","!",res)

print(res)