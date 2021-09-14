import json
import os

os.system("cls")

with open('C:/Users/João Marcos/Documents/João Marcos - Cotec/Python/jogador.json') as f:#alias
        jogador=json.load(f)

#chaves

for c in jogador:
    print(c)
print("-------------------------------------")
#valores
for v in jogador.values():
    print(v)
print("-------------------------------------")
#itens

for i in jogador.items():
    print(i)
print("-------------------------------------")

#itens da mochila
for i in jogador["mochila"]:
    print(i)
print("-------------------------------------")

#aeronaves
for a in jogador["aeronaves"]:
    print(a["tipo"]+" - "+str(a["habilidade"]))