import json
import os

os.system("cls")

carros_json='{"marca":"HRV","modelo":"Honda"}'#cria string no modelo JSON

carros=json.loads(carros_json)#converta para um dictionary

print(carros)

for i in carros:
    print(i)

for i in carros.values():
    print(i)

for k,v in carros.items():
    print(k,v)

car1={"marca":"kkk",
    "Chama":"Rodrigão"
    }

ca1_json=json.dumps(car1)
print(ca1_json)