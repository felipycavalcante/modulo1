# importa a lib para obter as tabelas da Wikipedia
from  lib.scrapy_table import Scrapy_Table
# Variavel com link da tabela
url="https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"
# Inicia a class para obter tabela
site_connect = Scrapy_Table(url)
# Pegando a tabela
tables = site_connect.get_tables(0)
  
# Listando conteudo da tabela
for linha in tables[1:]:

     # Obter o nome
     mun = linha[2]
     
     hab=int(linha[4])
 
     if(hab < 70000):
       print(mun[0:35])
