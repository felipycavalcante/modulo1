from  lib.scrapy_table import Scrapy_Table
# Variavel com o link da tabela
url="https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"
site_connect = Scrapy_Table(url)
tables = site_connect.get_tables(0)
  
# Listando o conteudo da tabela
for linha in tables[1:]:

     # Obtendo número e nome
     nome = linha[1]
     nome2 = linha[2]

     # Imprimindo os caracteres
     print(nome[0:15], nome2[0:35])
