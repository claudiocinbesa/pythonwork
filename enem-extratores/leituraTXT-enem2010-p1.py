import csv
# converte TXT para CSV  (Dados Enem 2010)
#fileOrig = 'D:\dct\enem-microdados\microdados_enem2010\Dados Enem 2010\DADOS_ENEM_2010.txt'
path = 'D:/dct/enem-microdados'
arq='DADOS_ENEM_2010'
fileOrig = path + '/microdados_enem2010/Dados Enem 2010/'+arq+'.txt'
fileTarg = path + '/microdados_enem2010/'+arq+'.csv'

f1 = open(fileOrig, 'r')
f2 = csv.writer(open(fileTarg, "wb"))

#grava o cabecalho
f2.writerow([
'NU_INSCRICAO',
'NU_ANO',
'IDADE',
'TP_SEXO',
'COD_MUNIC_INSC',
'NO_MUNICIPIO_INSC',
'UF_INSC',
'ST_CONCLUSAO',
'IN_TP_ENSINO',
'IN_CERTIFICADO',
'IN_BRAILLE',
'IN_AMPLIADA',
'IN_LEDOR',
'IN_ACESSO',
'IN_TRANSCRICAO',
'IN_LIBRAS',
'IN_UNIDADE_PRISIONAL',
'IN_BAIXA_VISAO',
'IN_CEGUEIRA',
'IN_DEFICIENCIA_AUDITIVA',
'IN_DEFICIENCIA_FISICA',
'IN_DEFICIENCIA_MENTAL',
'IN_DEFICIT_ATENCAO',
'IN_DISLEXIA',
'IN_GESTANTE',
'IN_LACTANTE',
'IN_LEITURA_LABIAL',
'IN_SABATISTA',
'IN_SURDEZ',
'TP_ESTADO_CIVIL',
'TP_COR_RACA',
'PK_COD_ENTIDADE',
'COD_MUNICIPIO_ESC',
'NO_MUNICIPIO_ESC',
'UF_ESC',
'ID_DEPENDENCIA_ADM',
'ID_LOCALIZACAO',
'SIT_FUNC',
'COD_MUNICIPIO_PROVA',
'NO_MUNICIPIO_PROVA',
'UF_CIDADE_PROVA',
'IN_PRESENCA_CN',
'IN_PRESENCA_CH',
'IN_PRESENCA_LC',
'IN_PRESENCA_MT',
'NU_NT_CN',
'NU_NT_CH',
'NU_NT_LC',
'NU_NT_MT',
'TX_RESPOSTAS_CN',
'TX_RESPOSTAS_CH',
'TX_RESPOSTAS_LC',
'TX_RESPOSTAS_MT',
'ID_PROVA_CN',
'ID_PROVA_CH',
'ID_PROVA_LC',
'ID_PROVA_MT',
'TP_LINGUA',
'DS_GABARITO_CN',
'DS_GABARITO_CH',
'DS_GABARITO_LC',
'DS_GABARITO_MT',
'IN_STATUS_REDACAO',
'NU_NOTA_COMP1',
'NU_NOTA_COMP2',
'NU_NOTA_COMP3',
'NU_NOTA_COMP4',
'NU_NOTA_COMP5',
'NU_NOTA_REDACAO'
])
i = 0
while 1:
    line_text = f1.readline()
    if line_text == "":
        break
    else:
        # grava dados em um CSV
        f2.writerow([  
            line_text[0:11 + 1].strip(), 
            line_text[12:15 + 1].strip(), 
            line_text[16:18 + 1].strip(), 
            line_text[19:19 + 1].strip(), 
            line_text[20:26 + 1].strip(), 
            line_text[27:176 + 1].strip(), 
            line_text[177:178 + 1].strip(), 
            line_text[179:179 + 1].strip(), 
            line_text[180:180 + 1].strip(), 
            line_text[181:181 + 1].strip(), 
            line_text[182:182 + 1].strip(), 
            line_text[183:183 + 1].strip(), 
            line_text[184:184 + 1].strip(), 
            line_text[185:185 + 1].strip(), 
            line_text[186:186 + 1].strip(), 
            line_text[187:187 + 1].strip(), 
            line_text[188:188 + 1].strip(), 
            line_text[189:189 + 1].strip(), 
            line_text[190:190 + 1].strip(), 
            line_text[191:191 + 1].strip(), 
            line_text[192:192 + 1].strip(), 
            line_text[193:193 + 1].strip(), 
            line_text[194:194 + 1].strip(), 
            line_text[195:195 + 1].strip(), 
            line_text[196:196 + 1].strip(), 
            line_text[197:197 + 1].strip(), 
            line_text[198:198 + 1].strip(), 
            line_text[199:199 + 1].strip(), 
            line_text[200:200 + 1].strip(), 
            line_text[201:201 + 1].strip(), 
            line_text[202:202 + 1].strip(), 
            line_text[203:210 + 1].strip(), 
            line_text[211:217 + 1].strip(), 
            line_text[218:367 + 1].strip(), 
            line_text[368:369 + 1].strip(), 
            line_text[370:370 + 1].strip(), 
            line_text[371:371 + 1].strip(), 
            line_text[372:372 + 1].strip(), 
            line_text[373:379 + 1].strip(), 
            line_text[380:529 + 1].strip(), 
            line_text[530:531 + 1].strip(), 
            line_text[532:532 + 1].strip(), 
            line_text[533:533 + 1].strip(), 
            line_text[534:534 + 1].strip(), 
            line_text[535:535 + 1].strip(), 
            line_text[536:544 + 1].strip(), 
            line_text[545:553 + 1].strip(), 
            line_text[554:562 + 1].strip(), 
            line_text[563:571 + 1].strip(), 
            line_text[572:616 + 1].strip(), 
            line_text[617:661 + 1].strip(), 
            line_text[662:706 + 1].strip(), 
            line_text[707:751 + 1].strip(), 
            line_text[752:754 + 1].strip(), 
            line_text[755:757 + 1].strip(), 
            line_text[758:760 + 1].strip(), 
            line_text[761:763 + 1].strip(), 
            line_text[764:764 + 1].strip(), 
            line_text[765:809 + 1].strip(), 
            line_text[810:854 + 1].strip(), 
            line_text[855:904 + 1].strip(), 
            line_text[905:949 + 1].strip(), 
            line_text[950:950 + 1].strip(), 
            line_text[951:959 + 1].strip(), 
            line_text[960:968 + 1].strip(), 
            line_text[969:977 + 1].strip(), 
            line_text[978:986 + 1].strip(), 
            line_text[987:995 + 1].strip(), 
            line_text[996:1004 + 1].strip()
            ])             
    i = i + 1
    # if i > 5:
        # break

f1.close()

