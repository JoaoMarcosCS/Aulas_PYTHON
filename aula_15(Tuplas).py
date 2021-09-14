#estrutura pra modificar uma tupla

t_num=(1,2,3,4,5,6)

for x in t_num:
    print(x)


l_num=list(t_num)
l_num[2]=4
t_num=tuple(l_num)

for x in t_num:
    print(x)
