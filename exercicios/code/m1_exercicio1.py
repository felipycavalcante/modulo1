'''
classe: m1_lab1.py
descricao: Listar os 3 primeiros caracteres do nome do vereador, pois em alguns casos o número disponível de caracteres é
apenas 3, e não 8, como estava anteriormente.
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data de entrega: 13/03/2019
'''

# importa a lib para obter as tabelas da Wikipedia
from  lib.scrapy_table import Scrapy_Table

# Variavel com o link da tabela
url="https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"

# Inicia a class para obter a tabela
site_connect = Scrapy_Table(url)

# Pegando a tabela 5 (Vereadores em exercicio)
tables = site_connect.get_tables(5)
  
# Listando o conteudo da tabela
for linha in tables[1:]:

     # Obtendo o nome. Esta na primeira posicao da lista
     nome = linha[0]

     # Imprimindo os caracteres da posicao 0 ate 2 (0, 1, 2 e 3) 
     print(nome[0:3])
