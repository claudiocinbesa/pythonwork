import sys, os
import time
from encoding.detectEncoding import *

datasetsPath = ["C:/tmp/enem/microdados_enem2009/Dados Enem 2009/DADOS_ENEM_2009.txt",
    "C:/tmp/enem/microdados_enem2009/Dados Enem 2009/QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2009.txt",
    "C:/tmp/enem/microdados_enem2010/Dados Enem 2010/DADOS_ENEM_2010.txt",
    "C:/tmp/enem/microdados_enem2010/Dados Enem 2010/QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010.txt",
    "C:/tmp/enem/microdados_enem2011/DADOS/DADOS_ENEM_2011.TXT",
    "C:/tmp/enem/microdados_enem2011/DADOS/QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2011.TXT",
    "C:/tmp/enem/microdados_enem2012/DADOS/DADOS_ENEM_2012.csv",
    "C:/tmp/enem/microdados_enem2012/DADOS/QUESTIONARIO_ENEM_2012.csv",
    "C:/tmp/enem/microdados_enem2013/DADOS/MICRODADOS_ENEM_2013.csv",
    "C:/tmp/enem/microdados_enem2013/DADOS/CONSISTENCIA_ENEM_ESCOLA_2013.csv",
    "C:/tmp/enem/microdados_enem2014/microdados_enem2014/DADOS/MICRODADOS_ENEM_2014.csv",
    "C:/tmp/enem/microdados_enem2014/microdados_enem2014/DADOS/CONSISTENCIA_ENEM_ESCOLA_2014.csv",
    "C:/tmp/enem/microdados_enem2015/microdados_enem_2015/DADOS/MICRODADOS_ENEM_2015.csv",
    "C:/tmp/enem/microdados_enem2015/microdados_enem_2015/DADOS/CONSISTENCIA_ENEM_ESCOLA_2015.CSV",
    "C:/tmp/enem/Microdados_enem_2016/DADOS/microdados_enem_2016.csv"]

datasetsPath1 = ['C:/tmp/enem/Microdados_enem_2016/DADOS/microdados_enem_2016.csv']

for file in datasetsPath:
    start = time.time()
    nameFile = file.split("/");
    data_file = file
    charSet = charsetEncoding(file)
    charDelimit = ''
    if nameFile[len(nameFile)-1].lower().find('.csv') >= 0:
        charDelimit = detectDelimiter(file)
    a_file = open(data_file)  
    cont = 0
    while 1:
        texto = a_file.readline()
        if texto == '':
            break
        try:
            cont = cont + 1
            nu_inscricao = texto[0:12]  
        except KeyError: 
            print "erro de leitura"
    a_file.close()
    finish = time.time()
    print   nameFile[len(nameFile)-1], cont, (finish - start), charSet, charDelimit