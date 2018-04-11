import psycopg2
con = psycopg2.connect(host='localhost', database='educ', user='postgres', password='postgres')
cur = con.cursor()
sql = 'create table enem.cidade (id serial primary key, nome varchar(100), uf varchar(2))'
cur.execute(sql)
sql = "insert into enem.cidade (nome, uf) values ('Sao Paulo', 'SP')"
cur.execute(sql)
con.commit()
cur.execute('select * from enem.cidade')
recset = cur.fetchall()
for rec in recset:
  print (rec)
con.close()