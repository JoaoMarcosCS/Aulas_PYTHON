import speech_recognition as sr
import os
import sys

os.system("cls")


def reconhece():
	rec = sr.Recognizer()# método junto com o Microphone para o input da voz

	with sr.Microphone() as s:
		rec.adjust_for_ambient_noise(s)

		while True:
			try:
				audio = rec.listen(s)#aqui que é o input da voz
				entrada = rec.recognize_google(audio, language="pt")#reconhece o idioma e dá o retorno
				return "Você disse: {}".format(entrada)
		

			except sr.UnknownValueError:# mensagem de erro
				return "Não entendi nada"
			

print("Ouvindo...\n-----------------\n")
fim=False
while fim==False:
	fala = reconhece()
	print(fala+str(type(fala)))
	if fala=="Você disse: encerrar":
		print("1")
		fim=True