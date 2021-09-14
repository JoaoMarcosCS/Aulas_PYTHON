num=res=i=0
canal="CFB CURSOS"

def cn():
    print(canal)

cn()

def cn2():
    kkk="escopo dentro da função cn2"
    print(kkk)

cn2()#único modo de usarmos a váriavel kkk

def cn3():
    global k
    k="colocando o escopo global na frente da varíavel, deixamos ela com esocpo globais"

cn3()#temos que colocar a chamda da função pois senão, não iremos declarar a varíavel k como global

print(k)