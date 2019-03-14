'''
classe: m1_lab4.py
descricao: Pesquisar se tem algum vereador vereador com os seguintes nomes (André, Rute, Aline)
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 13/03/2019
'''

# importa a lib para obter as tabelas da Wikipedia
from  lib.scrapy_table import Scrapy_Table


# Variavel com o link da tabela
url="https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"

# Inicia a class para obter a tabela
site_connect = Scrapy_Table(url)

# Pegando a tabela 5 (Vereadores em exercicio)
tables = site_connect.get_tables(5)
  
#Variavél para somatória de votos
total = 0 

for linha in tables[1:]:

    # Obtendo o numo de votos do cantidato
    nome = linha[0]

    # Separando o nome e sobrenome e tornando uma lista
    l_nome  = nome.split(" ")
          
    # Compara se é igual ao primeiro nome da lista. Lower muda a string para minuscula
    if 'andré' == l_nome[0].lower():
        print(nome)
          
    if 'rute' == l_nome[0].lower():
        print(nome)

    if 'aline' == l_nome[0].lower():
        print(nome)
