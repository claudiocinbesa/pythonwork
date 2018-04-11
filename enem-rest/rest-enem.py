from flask import Flask, make_response, jsonify, render_template
import psycopg2
import json

app = Flask(__name__)
    
@app.route("/json/idades/<ano>")
def getIdades(ano):
    con = psycopg2.connect(host='localhost', database='educ',
                           user='postgres', password='postgres')
    cur = con.cursor()

    sql = ""
    if (ano=='2014'):
          # sql = 'select idade, count(*) as quant from enem.enem_'+ano+' group by idade order by 1'
        sql = 'select idade, 1 as quant from enem.enem_'+ano+' LIMIT 1000'
    else:
        if(ano=='2015'):
            sql = 'select nu_idade as idade, count(*) as quant from enem.enem_'+ano+' group by nu_idade order by 1'
    cur.execute(sql)
    recset = cur.fetchall()
    con.close()
    return jsonify(faixas=recset, total=len(recset))
     
@app.route("/json/faixaetaria/<ano>")
def getFaixaEtaria(ano):
    if (ano=='2014'):
        my_query = query_db("SELECT " + 
                            "CASE " +
                            "  WHEN CAST(idade AS INT)<19 THEN '1-ATE 18' " +
                            "  WHEN CAST(idade AS INT)>20 THEN '3-ACIMA 21' " +
                            "  ELSE '2-ENTRE 19-20' " +
                            "END  AS fx, COUNT(*) as quant " +
                            "FROM enem.enem_2014  " +
                            "GROUP BY 1 ORDER BY 1" )
    else:
        if (ano =='2015' or ano=='2016'):
            my_query = query_db("SELECT " + 
                            "CASE " +
                            "  WHEN CAST(nu_idade AS INT)<19 THEN '1-ATE 18' " +
                            "  WHEN CAST(nu_idade AS INT)>20 THEN '3-ACIMA 21' " +
                            "  ELSE '2-ENTRE 19-20' " +
                            "END  AS fx, COUNT(*) as quant " +
                            "FROM enem.enem_"+ano+"  " +
                            "GROUP BY 1 ORDER BY 1" )

    json_output = json.dumps(my_query)
    return jsonify(my_query)                         # json_output

def db():
    con = psycopg2.connect(host='localhost', database='educ',
                           user='postgres', password='postgres')
    
    return con

def query_db(query):
    cur = db().cursor()
    cur.execute(query)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return r  # (r[0] if r else None)

if __name__ == "__main__":
    app.run(debug=True)