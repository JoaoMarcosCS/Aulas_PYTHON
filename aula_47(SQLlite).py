import  sqlite3
from sqlite3 import Error
import os

os.system("cls")

caminho="C:/Users/João Marcos/Documents/João Marcos - Cotec/DBS-SQLlite/tabela.db"

def conexao(caminho):
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as erro:
        print(erro)
    
    return con

conectou=conexao(caminho)



com_slq="""CREATE TABLE tb_contatos(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contato VARCHAR(30),
        telefone INTEGER,
        email VARCHAR(30)
        
        );"""

def cria_tb(conexao,sql):
    try:
        c=conexao.cursor()#criando o objeto para executar os comandos slq
        c.execute(sql)
    except Error as erro:
        print(erro)

c_tb=cria_tb(conectou,com_slq)


conectou.close()