import csv
import time 

fileCSV = 'D:\dct\enem-microdados\microdados_enem2015\DADOS\MICRODADOS_ENEM_2015.csv';
print "\nDADOS ..."
data = csv.reader(open(fileCSV, 'r')) 
i = 0
start = time.time()
#imprimir primeiras linhas 
for row in data: 
    i = i + 1
    if (i == 1):
        print str(row) 
        
finish = time.time()       
print ("Tempo decorrido = " + str(finish - start) );    
print("\n TOTAL DE LINHAS = " +  str(i) + " ***FIM***")