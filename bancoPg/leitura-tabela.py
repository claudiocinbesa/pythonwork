import psycopg2
import matplotlib.pyplot as plt
import pandas as pd

con = psycopg2.connect(host='localhost', database='educ', user='postgres', password='postgres')
cur = con.cursor()
cur.execute('select idade, count(*) from enem.enem_2014 group by idade order by 1')
recset = cur.fetchall()
for rec in recset:
  print (rec)
con.close()

