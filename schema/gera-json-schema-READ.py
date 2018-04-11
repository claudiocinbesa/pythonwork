from tableschema import Table

fileCSV = 'D:\dct\enem-microdados\DADOS_ENEM_2009.csv'
fileJSON = 'D:\dct\enem-microdados\DADOS_ENEM_2009.json'


# Create table
table = Table(fileCSV, schema=fileJSON)

# Print schema descriptor
print(table.schema.descriptor) 
print "\n"
# Print cast rows in a dict form
for keyed_row in table.iter(keyed=True):
    print(keyed_row)
    print "\n"