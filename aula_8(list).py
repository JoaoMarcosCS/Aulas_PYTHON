carros=["1","2","3","4"]
carros[3]="5"
carros.append("6")
carros.remove("6")
carros.pop()#remove a última posição 
del carros[0]#remove com indexação

print("Quantidados de números:"+str(len(carros)))
print("Números: "+str(carros))


carros2=list(carros)#copia os dados

carros3=carros+carros2

carros.clear()


print("Quantidados de números:"+str(len(carros3)))
print("Números: "+str(carros3))
print("Quantidados de números:"+str(len(carros2)))
print("Números: "+str(carros2))
print("Quantidados de números:"+str(len(carros)))
print("Números: "+str(carros))