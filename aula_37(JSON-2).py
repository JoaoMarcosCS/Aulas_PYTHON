import os 
import json

os.system("cls")

carros_dic={
    "marca":"honda",
    "preco":199.99,
    "nome":"cartola"
}
#dic -> objeto json


carros_list=["honda","mercedes","camaro"]
#list -> array json

carros_tu=("honda","mercedes","camaro")
#tupla -> array json

#numero -> numeros 
#strings -> strings

carros_j=json.dumps(carros_dic,indent=20,separators=(": ","=="),sort_keys=True)
"""
indent recuo da borda
separators muda o sepador chave-valor
sort_keys ordena as chaves

"""

print(carros_j)

