import os

carros=[]

class Carro:
    nome=""
    pot=0
    velmax=0
    ligado=False
    def __init__(self,nome,pot):
        self.nome=nome
        self.pot=pot
        self.velmax=int(pot)*2
        self.ligado=False

    def ligar(self):
        self.ligado=True
    
    def desligar(self):
        self.ligado=False

    def info(self):
        print("Nome........:"+self.nome)
        print("Potência....:"+str(self.pot))
        print("Vel.máxima..:"+str(self.velmax))
        print("Ligado......:"+("sim" if self.ligado==True else "não"))

    def help(self):
        print("new - Novo Carro")
        print("info - Informações do Carro")
        print("del - Exclui o Carro")
        print("on - Liga o carro")
        print("off - Deslga o Carro")
        print("ls - Lista os Carros")
        print("help - Mostra os comandos disponiveis")
        print("out - Sair")


def Menu():
    os.system("cls") or None
    print("new - Novo Carro")
    print("info - Informações do Carro")
    print("del - Exclui o Carro")
    print("on - Liga o carro")
    print("off - Deslga o Carro")
    print("ls - Lista os Carros")
    print("help - Mostra os comandos disponiveis")
    print("out - Sair")
    print("Quantidade de Carros: "+str(len(carros)))
    opc=input("user@none:~# ")
    return opc
    
def NovoCarro():
    os.system("cls") or None
    n=input("Nome do Carro...:")
    p=input("Potêcia do Carro:")
    car=Carro(n,p)
    carros.append(car)
    print("Novo carro criado")
    os.system("pause")

def Informações():
    os.system("cls") or None
    n=input("Numero do Carro...:")

    try:
        carros[int(n)].info()
    except:
        print("Carro não encontrado")
    os.system("pause")

def excluiCarro():
    os.system("cls") or None
    n=input("Numero do Carro...:")

    try:
        del carros[int(n)]
    except:
        print("Carro não encontrado")
    os.system("pause")


def ligarCarro():
    os.system("cls") or None
    n=input("Numero do Carro...:")

    try:
        carros[int(n)].ligar()
        print("Carro "+str(carros[int(n)])+" ligado")
    except:
        print("Carro não encontrado")
    os.system("pause")


def desligarCarro():
    os.system("cls") or None
    n=input("Numero do Carro...:")

    try:
        carros[int(n)].desligar()
        print("Carro "+str(carros[int(n)])+" delisgado")
    except:
        print("Carro não encontrado")
    os.system("pause")

def listarCarros():
    os.system("cls")
    p=0
    for car in carros:
        print(str(p)+" - "+car.nome)
        p=p+1
    os.system("pause")
    os.system("cls")

ret=Menu()

while ret!="out":

    if ret=="new":
        NovoCarro()
    elif ret=="info":
        Informações()
    elif ret=="del":
        excluiCarro()
    elif ret=="on":
        ligarCarro()
    elif ret=="off":
        desligarCarro()
    elif ret=="ls":
        listarCarros()
    
    ret=Menu()

print("Bye bye")
    



