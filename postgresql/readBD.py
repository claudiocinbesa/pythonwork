import psycopg2
try:
    conn = psycopg2.connect("dbname='educ' user='postgres' host='localhost' password='postgres'")
except:
    print "I am unable to connect to the database"
sql = "select *  from enem.dados_enem_2009 limit 100"
cursor = conn.cursor()
# Fetch all rows from table
cursor.execute(sql)
rows = cursor.fetchall()

# Print all rows
for row in rows:
    print "Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2]))

# Cleanup
conn.commit()
cursor.close()
conn.close()