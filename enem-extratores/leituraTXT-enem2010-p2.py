import csv
# converte TXT para CSV  (dados socioeconomicos ENEM 2010)
#fileOrig = 'D:\dct\enem-microdados\microdados_enem2010\Dados Enem 2010\DADOS_ENEM_2010.txt'
#fileTarg = 'D:\dct\enem-microdados\DADOS_ENEM_2010.csv'
path = 'D:/dct/enem-microdados'
arq = 'QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2010'
fileOrig = path + '/microdados_enem2010/Dados Enem 2010/'+arq+'.txt'
fileTarg = path + '/microdados_enem2010/'+arq+'.csv'

f1 = open(fileOrig, 'r')
f2 = csv.writer(open(fileTarg, "wb"))
print ("gerando CSV de " + arq)

#grava o cabecalho
f2.writerow([ 
'NU_INSCRICAO',
'IN_QSE',
'Q01',
'Q02',
'Q03',
'Q04',
'Q05',
'Q06',
'Q07',
'Q08',
'Q09',
'Q10',
'Q11',
'Q12',
'Q13',
'Q14',
'Q15',
'Q16',
'Q17',
'Q18',
'Q19',
'Q20',
'Q21',
'Q22',
'Q23',
'Q24',
'Q25',
'Q26',
'Q27',
'Q28',
'Q29',
'Q30',
'Q31',
'Q32',
'Q33',
'Q34',
'Q35',
'Q36',
'Q37',
'Q38',
'Q39',
'Q40',
'Q41',
'Q42',
'Q43',
'Q44',
'Q45',
'Q46',
'Q47',
'Q48',
'Q49',
'Q50',
'Q51',
'Q52',
'Q53',
'Q54',
'Q55',
'Q56',
'Q57'
])
i = 0
while 1:
    line_text = f1.readline()
    if line_text == "":
        break
    else:
        # recupera as variaveis e        
        # grava dados em um CSV
        f2.writerow([  
            line_text[0:11 + 1].strip(), 
            line_text[12:12 + 1].strip(), 
            line_text[13:13 + 1].strip(), 
            line_text[14:14 + 1].strip(), 
            line_text[15:15 + 1].strip(), 
            line_text[16:16 + 1].strip(), 
            line_text[17:17 + 1].strip(), 
            line_text[18:18 + 1].strip(), 
            line_text[19:19 + 1].strip(), 
            line_text[20:20 + 1].strip(), 
            line_text[21:21 + 1].strip(), 
            line_text[22:22 + 1].strip(), 
            line_text[23:23 + 1].strip(), 
            line_text[24:24 + 1].strip(), 
            line_text[25:25 + 1].strip(), 
            line_text[26:26 + 1].strip(), 
            line_text[27:27 + 1].strip(), 
            line_text[28:28 + 1].strip(), 
            line_text[29:29 + 1].strip(), 
            line_text[30:30 + 1].strip(), 
            line_text[31:31 + 1].strip(), 
            line_text[32:32 + 1].strip(), 
            line_text[33:33 + 1].strip(), 
            line_text[34:34 + 1].strip(), 
            line_text[35:35 + 1].strip(), 
            line_text[36:36 + 1].strip(), 
            line_text[37:37 + 1].strip(), 
            line_text[38:38 + 1].strip(), 
            line_text[39:39 + 1].strip(), 
            line_text[40:40 + 1].strip(), 
            line_text[41:41 + 1].strip(), 
            line_text[42:42 + 1].strip(), 
            line_text[43:43 + 1].strip(), 
            line_text[44:44 + 1].strip(), 
            line_text[45:45 + 1].strip(), 
            line_text[46:46 + 1].strip(), 
            line_text[47:47 + 1].strip(), 
            line_text[48:48 + 1].strip(), 
            line_text[49:49 + 1].strip(), 
            line_text[50:50 + 1].strip(), 
            line_text[51:51 + 1].strip(), 
            line_text[52:52 + 1].strip(), 
            line_text[53:53 + 1].strip(), 
            line_text[54:54 + 1].strip(), 
            line_text[55:55 + 1].strip(), 
            line_text[56:56 + 1].strip(), 
            line_text[57:57 + 1].strip(), 
            line_text[58:58 + 1].strip(), 
            line_text[59:59 + 1].strip(), 
            line_text[60:60 + 1].strip(), 
            line_text[61:61 + 1].strip(), 
            line_text[62:62 + 1].strip(), 
            line_text[63:63 + 1].strip(), 
            line_text[64:64 + 1].strip(), 
            line_text[65:65 + 1].strip(), 
            line_text[66:66 + 1].strip(), 
            line_text[67:67 + 1].strip(), 
            line_text[68:68 + 1].strip(), 
            line_text[69:69 + 1].strip()
            ])             
    i = i + 1
    # if i > 5:
        # break

f1.close()

