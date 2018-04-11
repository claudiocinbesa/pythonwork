import pandas as pd
import matplotlib.pyplot as plt
import os
import urllib
import csv 
from helperSchema.detectEncoding import *

plt.style.use('ggplot')

cache = 'cache'
if not os.path.exists(cache):
    os.makedirs(cache)

dest = os.path.join(cache, 'inpc-a.csv')
# recupera os dados do INPC-A do Banco Central (usa ; como delimitador e , como ponto decimal)
urllib.urlretrieve('http://api.bcb.gov.br/dados/serie/bcdata.sgs.11428/dados?formato=csv',
        dest)


fileCSV = dest
# './data/censopessoa.csv'
delim = detectDelimiter(fileCSV)
df =  pd.read_csv(fileCSV, sep=delim)

#Quantidade de linhas e colunas do DataFrame
df.shape
#Descricao do Index
df.index 
#Colunas presentes no DataFrame
print "\nCOLUNAS = "
print ( df.columns) 
#Contagem de dados nao-nulos
print (df.count())

#resumo
print  "\nRESUMO"
print (df.describe())

print "\nDADOS ..."
data = csv.reader(open(fileCSV, 'r')) 
i = 0
#imprimir primeiras linhas 
for rows in data: 
    i = i + 1
    print rows 
    if i == 2: 
       break
print("FIM***")
