import sqlite3
from sqlite3 import Error
import os

os.system("cls")

def conexao():
    caminho="C:/Users/João Marcos/Documents/João Marcos - Cotec/DBS-SQLlite/tabela.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as erro:
        print(erro)
    return con

vcon=conexao()

