import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/educ')
connection = engine.connect()
result = connection.execute("select sg_uf_residencia from enem.enem_2015 limit 10")
for row in result:
    print ("sg_uf_residencia:" + row['sg_uf_residencia'])
connection.close()