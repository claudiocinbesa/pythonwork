import io
import csv
import datapackage
from jsontableschema import infer
# from helperSchema.detectEncoding import detectDelimiter, charsetEncoding
from helperSchema.detectEncoding import *

dp = datapackage.DataPackage()
filepath = 'D:/dct/enem-microdados/microdados_enem2016/Microdados_enem_2016/DADOS/microdados_enem_2016.csv'
encod = charsetEncoding(filepath)
delim = detectDelimiter(filepath)
print encod + "  - " + delim
with io.open(filepath, encoding=encod) as stream:
    headers = stream.readline().rstrip('\n').split(delim)
    print headers
    values = csv.reader(stream)
    print values

    # schema = infer(headers, values)
    dp.descriptor['resources'] = [
        {
            'name': 'data',
            'path': filepath,
            # 'schema': schema
        }
    ]