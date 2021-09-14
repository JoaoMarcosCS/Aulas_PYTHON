import os

os.system("cls")

try:
    print(x)

except NameError:# NameErros é um expection usado quando uma váriavel não é definida
    print("X não foi definida")

except:
    print("Erro não definido")

else:#faz alguma coisa caso o try seja bem sucedido
    print("Tudo certo")

finally:#o código que estiver aqui vai ser executado independentemente do try ou except
    print("FIM")

x=-10

if x<1:
    