import random

num_i=5
num_f=5.8
num_c=1j
 
x=int(num_f)

print("Valor: "+str(x)+" - Tipo: "+str(type(x)))

num_r=random.randrange(0,765)
x=num_r

print("Valor: "+str(x)+" - Tipo: "+str(type(x)))

num_ar=[
    random.randrange(0,765),
    random.randrange(0,765),
    random.randrange(0,765),
    random.randrange(0,765),
    random.randrange(0,765),
    random.randrange(0,765),
    random.randrange(0,765)

]

x=num_ar

print("Valor: "+str(x[3])+" - Tipo: "+str(type(x)))