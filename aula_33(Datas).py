import os
import datetime

os.system("cls")

data=datetime.datetime.now()

nasc=datetime.datetime(1978,3,7)

print(str(data.day)+"/"+str(data.month)+"/"+str(data.year))
print(nasc.strftime("%A"))
print("heelo"*5)#imprime 5 vezes o heelo

"""
%a - texto dia da semana abreviado
%A - texto dia da semana
%w - num dia da semana
%d - num dia do mes
%b - texto mes abreviado
%B - texto mes
%m - num do mes
%y - ano com dois digitos
%Y - ano com quatro fdigitos
%H - 00 - 23
%I - 00 -12
%p - AM/PM
%M - minutos
%S - secundos
%f - microsegundos
%j - dia do ano 000 - 366
%W - dia da semana no ano
"""