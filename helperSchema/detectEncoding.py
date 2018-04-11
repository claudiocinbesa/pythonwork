import chardet
import urllib
import csv

# return the encoding from urlFile
def charsetEncoding(pathFile):
    f = open(pathFile)
    i = 0
    codMap = {}
    while 1:
        textLine = f.readline()
        i = i + 1
        if textLine == "" or i >= 400:
            break
        # detect charset in textLine
        result = chardet.detect(textLine)
        if result['encoding'] in codMap:
            codMap[result['encoding']] = codMap[result['encoding']] + 1
        else:
            codMap[result['encoding']] = 1
    f.close()
    # remove  'ascii' pattern (default) 
    if ('ascii' in codMap) and (len(codMap) > 1):
        del codMap['ascii']
	# return the most frequent charset encoding
    return max(codMap, key=codMap.get) 

def detectDelimiter(filename_input):
    with open(filename_input, 'r') as f1:
        #dialect = csv.Sniffer().sniff(f1.read())
        dialect = csv.Sniffer().sniff(f1.readline(), [',',';','|','\t',':'])
        f1.seek(0)
        return dialect.delimiter

# url = 'http://yahoo.co.jp/'
#url = 'C:/tmp/enem/Microdados_enem_2016/DADOS/microdados_enem_2016.csv'
#url = 'C:/tmp/enem/csv1966-1995.csv' 
#url ='C:/tmp/enem/ESCOLAS-censo-2016.CSV' 
#print charsetEncoding(url)