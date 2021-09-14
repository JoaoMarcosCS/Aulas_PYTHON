carros=["1","2","3","4","5"]

itCarros=iter(carros)

print(next(itCarros))
print(next(itCarros))
print(next(itCarros))
print(next(itCarros))
print(next(itCarros))

itCarros2=iter(carros)

while itCarros:
    try:
        print(next(itCarros2))
    except StopIteration:
        print("Fim da lista")
        break
