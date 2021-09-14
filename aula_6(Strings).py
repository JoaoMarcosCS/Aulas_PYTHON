curso="Curso de python!!!"

print("Tamanho:"+str(len(curso)))
print(curso)
print("Diferença usando o strip(remove os espaços):"+curso.strip())
print("Minúsculo:"+curso.lower().strip())
print("Maiúsculo:"+curso.upper().strip())
print("Trocando python por C#:"+curso.replace("python","C#"))
curso.replace("python","C#")
print(curso)
print(curso[9:15])
a=curso.split(" ")
print("Cortando as strings:"+a[0]+a[1]+a[2])

encontrou="python" in curso#eu poderia colocar not in curso, que retornaria false
print("Python está na string: "+str(encontrou))

texto="Eu gosto de X-bacon"
palavra="x-bacon"

encontrou=palavra.upper() in texto.upper()

print(str(encontrou))

concatenacao=texto+" com "+palavra+" extra"
print("Texto cancatenado: "+concatenacao)

cidade="Aparecida"
dia=15
mes="Abril"
ano=2025
canal="CFB"
data="{}, {} de {} de {} \n \"{}\" "
"""
\'\' - imprime os apotrfos
\"\" - imprime as aspas
\n - pula linha
\r -?
\t - tabulação
\b - back space 

"""

print("Formatação para data: "+data.format(cidade,dia,mes,ano,canal))

