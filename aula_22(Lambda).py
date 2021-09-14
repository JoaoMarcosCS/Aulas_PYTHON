import os

os.system("cls")

#sintaxe da lambda

soma=lambda a,b:a+b#argumento:retorno

print(soma(1,2))

r=lambda x,func:x+func(x)
res=r(2,lambda x:x*x)
print(res)