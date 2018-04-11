import csv
fileOrig = 'D:\dct\enem-microdados\microdados_enem2009\Dados Enem 2009\DADOS_ENEM_2009.txt'
fileTarg = 'D:\dct\enem-microdados\DADOS_ENEM_2009.csv'
f1 = open(fileOrig, 'r')
#f2 = open(fileTarg, 'w')
f2 = csv.writer(open(fileTarg, "wb"))

#grava o cabecalho
f2.writerow(['NU_INSCRICAO', 
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
'IN_OUTRO', 
'IN_LIBRAS', 
'IN_UNIDADE_PRISIONAL', 
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
'NU_NOTA_REDACAO'])
i = 0
while 1:
    line_text = f1.readline()
    if line_text == "":
        break
    else:
        # recupera as variaveis
        NU_INSCRICAO = line_text[0:11 + 1].strip()
        NU_ANO = line_text[12:15 + 1].strip()
        IDADE = line_text[16:18 + 1].strip()
        TP_SEXO = line_text[19:19 + 1].strip()
        COD_MUNIC_INSC = line_text[20:26 + 1].strip()
        NO_MUNICIPIO_INSC = line_text[27:176 + 1].strip()
        UF_INSC = line_text[177:178 + 1].strip()
        ST_CONCLUSAO = line_text[179:179 + 1].strip()
        IN_TP_ENSINO = line_text[180:180 + 1].strip()
        IN_CERTIFICADO = line_text[181:181 + 1].strip()
        IN_BRAILLE = line_text[182:182 + 1].strip()
        IN_AMPLIADA = line_text[183:183 + 1].strip()
        IN_LEDOR = line_text[184:184 + 1].strip()
        IN_ACESSO = line_text[185:185 + 1].strip()
        IN_TRANSCRICAO = line_text[186:186 + 1].strip()
        IN_OUTRO = line_text[187:187 + 1].strip()
        IN_LIBRAS = line_text[188:188 + 1].strip()
        IN_UNIDADE_PRISIONAL = line_text[189:189 + 1].strip()
        PK_COD_ENTIDADE = line_text[190:197 + 1].strip()
        COD_MUNICIPIO_ESC = line_text[198:204 + 1].strip()
        NO_MUNICIPIO_ESC = line_text[205:354 + 1].strip()
        UF_ESC = line_text[355:356 + 1].strip()
        ID_DEPENDENCIA_ADM = line_text[357:357 + 1].strip()
        ID_LOCALIZACAO = line_text[358:358 + 1].strip()
        SIT_FUNC = line_text[359:359 + 1].strip()
        COD_MUNICIPIO_PROVA = line_text[360:366 + 1].strip()
        NO_MUNICIPIO_PROVA = line_text[367:516 + 1].strip()
        UF_CIDADE_PROVA = line_text[517:518 + 1].strip()
        IN_PRESENCA_CN = line_text[519:519 + 1].strip()
        IN_PRESENCA_CH = line_text[520:520 + 1].strip()
        IN_PRESENCA_LC = line_text[521:521 + 1].strip()
        IN_PRESENCA_MT = line_text[522:522 + 1].strip()
        NU_NT_CN = line_text[523:531 + 1].strip()
        NU_NT_CH = line_text[532:540 + 1].strip()
        NU_NT_LC = line_text[541:549 + 1].strip()
        NU_NT_MT = line_text[550:558 + 1].strip()
        TX_RESPOSTAS_CN = line_text[559:603 + 1].strip()
        TX_RESPOSTAS_CH = line_text[604:648 + 1].strip()
        TX_RESPOSTAS_LC = line_text[649:693 + 1].strip()
        TX_RESPOSTAS_MT = line_text[694:738 + 1].strip()
        ID_PROVA_CN = line_text[739:740 + 1].strip()
        ID_PROVA_CH = line_text[741:742 + 1].strip()
        ID_PROVA_LC = line_text[743:744 + 1].strip()
        ID_PROVA_MT = line_text[745:746 + 1].strip()
        DS_GABARITO_CN = line_text[747:791 + 1].strip()
        DS_GABARITO_CH = line_text[792:836 + 1].strip()
        DS_GABARITO_LC = line_text[837:881 + 1].strip()
        DS_GABARITO_MT = line_text[882:926 + 1].strip()
        IN_STATUS_REDACAO = line_text[927:927 + 1].strip()
        NU_NOTA_COMP1 = line_text[928:936 + 1].strip()
        NU_NOTA_COMP2 = line_text[937:945 + 1].strip()
        NU_NOTA_COMP3 = line_text[946:954 + 1].strip()
        NU_NOTA_COMP4 = line_text[955:963 + 1].strip()
        NU_NOTA_COMP5 = line_text[964:972 + 1].strip()
        NU_NOTA_REDACAO = line_text[973:981 + 1].strip()

        
        # grava dados em um CSV
        f2.writerow([  
            NU_INSCRICAO, 
            NU_ANO, 
            IDADE, 
            TP_SEXO, 
            COD_MUNIC_INSC, 
            NO_MUNICIPIO_INSC, 
            UF_INSC, 
            ST_CONCLUSAO, 
            IN_TP_ENSINO, 
            IN_CERTIFICADO, 
            IN_BRAILLE, 
            IN_AMPLIADA, 
            IN_LEDOR, 
            IN_ACESSO, 
            IN_TRANSCRICAO, 
            IN_OUTRO, 
            IN_LIBRAS, 
            IN_UNIDADE_PRISIONAL, 
            PK_COD_ENTIDADE, 
            COD_MUNICIPIO_ESC, 
            NO_MUNICIPIO_ESC, 
            UF_ESC, 
            ID_DEPENDENCIA_ADM, 
            ID_LOCALIZACAO, 
            SIT_FUNC, 
            COD_MUNICIPIO_PROVA, 
            NO_MUNICIPIO_PROVA, 
            UF_CIDADE_PROVA, 
            IN_PRESENCA_CN, 
            IN_PRESENCA_CH, 
            IN_PRESENCA_LC, 
            IN_PRESENCA_MT, 
            NU_NT_CN, 
            NU_NT_CH, 
            NU_NT_LC, 
            NU_NT_MT, 
            TX_RESPOSTAS_CN, 
            TX_RESPOSTAS_CH, 
            TX_RESPOSTAS_LC, 
            TX_RESPOSTAS_MT, 
            ID_PROVA_CN, 
            ID_PROVA_CH, 
            ID_PROVA_LC, 
            ID_PROVA_MT, 
            DS_GABARITO_CN, 
            DS_GABARITO_CH, 
            DS_GABARITO_LC, 
            DS_GABARITO_MT, 
            IN_STATUS_REDACAO, 
            NU_NOTA_COMP1, 
            NU_NOTA_COMP2, 
            NU_NOTA_COMP3, 
            NU_NOTA_COMP4, 
            NU_NOTA_COMP5, 
            NU_NOTA_REDACAO
            ])             
    i = i + 1
    # if i > 5:
        # break

f1.close()

