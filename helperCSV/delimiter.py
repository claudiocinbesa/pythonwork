import csv

def detectDelimiter(filename_input):
    with open(filename_input, 'r') as f1:
        #dialect = csv.Sniffer().sniff(f1.read())
        dialect = csv.Sniffer().sniff(f1.readline(), [',',';','|','\t',':'])
        f1.seek(0)
        return dialect.delimiter


# filename_input = 'C:/tmp/enem/Microdados_enem_2016/DADOS/microdados_enem_2016.csv'
# filename_input = 'C:/tmp/enem/csv1966-1995.csv' 
# filename_input   = 'C:/tmp/enem/ESCOLAS-censo-2016.CSV'
