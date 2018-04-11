_CONNECT_URL = "host=localhost dbname=educ user=postgres password=postgres"

def geraSchema(csvFile, tabelName):
    from tableschema import Table
    import json
    # abre o CSV
    table = Table(csvFile)
    #, schema='schema.json')

    table.infer(limit=100000)
    json_data = table.schema.descriptor
    # print json_data.keys()
    sqlCommand = "DROP TABLE IF EXISTS "+ tabelName + "; \n" + "CREATE TABLE " + tabelName + " ( " + "\n"
    t = len(json_data['fields'])
    cont = 0
    for campos in json_data['fields']:
        cont = cont + 1
        comma = ","
        if (cont == t):
            comma = " "
        typeData = campos['type']
        if (campos['name'] == "NU_INSCRICAO"):
            typeData = "varchar(12)"
        else:
            if (typeData == "string"):
                typeData = "varchar"
            else:
                if (typeData == "number"):
                    typeData = "varchar(20)" # "numeric(7,2)"
                else:
                    if (typeData == "integer"):
                        typeData = "varchar(10)"
        sqlCommand = sqlCommand + "\t" + \
            campos['name'] + "\t" + typeData + comma + "\n"

    sqlCommand = sqlCommand + "); \t"
    # print sqlCommand
    return sqlCommand


def criaSchemaDB(sqlCommand):
    import psycopg2
    conn = psycopg2.connect(_CONNECT_URL)
    cur = conn.cursor()
    cur.execute(sqlCommand)
    conn.commit()
    return


def loadTabelFromCSV(csvFile, tableName):
    import psycopg2
    conn = psycopg2.connect(_CONNECT_URL)
    cur = conn.cursor()
    sqlCommand = "COPY " + tableName + " from '" + csvFile +"' HEADER CSV encoding 'ISO-8859-1';"
    cur.execute(sqlCommand)
    conn.commit()
    return

def geraTabela(csvFile, tableName):
    import psycopg2
    conn = psycopg2.connect(_CONNECT_URL)
    cur = conn.cursor()
    with open(csvFile, 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f)  # Skip the header row.
        # faz a copia para o banco de dados mas so funciona se o encode="UTF8"
        cur.copy_from(f, tableName, sep=',')

    conn.commit()
    return

print "Rotinas de carga de dados na base Educ postgresql."
csvFile = 'd:\dct\enem-microdados\microdados_enem2012\DADOS\DADOS_ENEM_2012.csv'
criaSchemaDB(geraSchema(csvFile, "enem2012"))
loadTabelFromCSV(csvFile, 'enem2012')
