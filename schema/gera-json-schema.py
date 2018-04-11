from tableschema import Table

fileCSV = 'D:\dct\enem-microdados\DADOS_ENEM_2009.csv'
fileJSON = 'D:\dct\enem-microdados\DADOS_ENEM_2009-schema.json'

# Create table
table = Table(fileCSV)
table.infer(limit=100000)
# table.schema.descriptor
table.schema.save(fileJSON)