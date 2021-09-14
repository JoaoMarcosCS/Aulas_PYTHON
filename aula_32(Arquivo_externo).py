import externo as ex#se tivesse em outro diretório, eu teria que colocar o caminho
import os
from externo import jogador#com isso, não precismos colocar o externo ou o ex na frente para acessarmos o jogador

os.system("cls")

#externo.canal()
ex.canal()

#print(externo.jogador["nome"])
#print(ex.jogador["nome"])
print(jogador["nome"])

res=dir(ex)#retorna todas as propriedaades da lib externo, até mesmo, suas funções 

print(res)