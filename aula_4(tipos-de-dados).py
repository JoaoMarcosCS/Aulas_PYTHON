#uma varíavel pode assumir vários tipos de dados de acordo com o decorrer do programa
x=1
x="CDFFF"
x=True
x=134.92
n1=5;n2=7
x=complex(n1,n2)#numero complexo

print("Valor: "+str(x))#str para colocar como string e imprimir
print(x.real)
print(x.imag)
print("Tipo de x:"+str(type(x)) )#str para fazer o typecast 

x=["Carro","Avião","Navio",1,14.8,True]#Lista/Array
x=("Carro","Avião","Navio",1,14.8)#Tupla, não podemos modificar os valores de uma tupla como em um array
x=range(0,100,1)#cria um list de 0 a 100 todos com valores 1
print("Novo valor de x:"+str(x[10]))
print("Tipo: "+str(type(x)))
x={#dicionary -> chave valor

    "canal":"CFB CURSOS",
    "curso":"python",
    "nome":"bruno"
}

print("Novo valor de x com chave curos:"+str(x["curso"]))
print("Tipo: "+str(type(x)))

x={5,4,2,5,7,7,4,3,2,34,5,6,7,7,4,3,2,2,5,6}#set -> não repete os valores
x=frozenset({5,4,2,5,7,7,4,3,2,34,5,6,7,7,4,3,2,2,5,6})#bloqueia o set para que  não seja modificado, como uma tupla

print("Novo valor de x:"+str(x))
print("Tipo: "+str(type(x)))


