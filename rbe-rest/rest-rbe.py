from flask import Flask, make_response, jsonify, render_template
import psycopg2
import json

app = Flask(__name__)


@app.route("/rbe/atendimentos/<ano>/<mes>")
def getAtendimentos(ano, mes):
    sql = "SELECT unidade, ano, mes, dia, munic || ' (' || uf || ')' AS munic, "
    sql = sql + " sexo, sala, fx_etaria, count(*) as quant "
    sql = sql + " FROM ( "
    sql = sql + " select DISTINCT u.descricaoabreviada as unidade,  "
    sql = sql + " f.codpaciente, f.uf, f.nome AS munic,  f.sexo, "
    sql = sql + " f.nomeinterno AS sala,   "
    sql = sql + " f.datanascimento, EXTRACT(YEAR FROM age(f.dataatendimento, f.datanascimento)) AS idade,  "
    sql = sql + " CASE WHEN EXTRACT(YEAR FROM age(f.dataatendimento, f.datanascimento)) <= 1 THEN 'A:(0 -  1) RECEM NASCIDO '  "
    sql = sql + "      WHEN EXTRACT(YEAR FROM age(f.dataatendimento, f.datanascimento)) <=11 THEN 'B:(1 - 11) INFANCIA '  "
    sql = sql + " 	 WHEN EXTRACT(YEAR FROM age(f.dataatendimento, f.datanascimento)) <=17 THEN 'C:(12 -17) ADOLESCENCIA '  "
    sql = sql + " 	 WHEN EXTRACT(YEAR FROM age(f.dataatendimento, f.datanascimento)) <=40 THEN 'D:(18 -40) ADULTO JOVEM '  "
    sql = sql + " 	 WHEN EXTRACT(YEAR FROM age(f.dataatendimento, f.datanascimento)) <=65 THEN 'E:(41 -65) ADULTO '  "
    sql = sql + "      ELSE 'F:(+65) IDOSO '  "
    sql = sql + " END AS fx_etaria,   "
    sql = sql + "  EXTRACT(YEAR FROM f.dataatendimento) as ano, "
    sql = sql + "  EXTRACT(MONTH FROM f.dataatendimento) as mes, "
    sql = sql + "  EXTRACT(DAY FROM f.dataatendimento) as dia "
    sql = sql + " from dbo.pas_filaatendimento AS f, "
    sql = sql + " dbo.pas_unidade as u "
    sql = sql + "  where "
    sql = sql + "  f.cnes = u.cnes "
    sql = sql + "   AND EXTRACT(YEAR FROM f.dataatendimento) = " + ano
    sql = sql + "   AND EXTRACT(MONTH FROM f.dataatendimento) = " + mes
    sql = sql + "   AND f.dataexclusao IS NULL "
    sql = sql + "   AND f.nomeinterno IN ('ClinicoGeral', 'Odontologia', 'Pediatria', 'ServicoSocial', 'Traumatologia', 'Urgencia')   "
    sql = sql + "  ) AS tp "
    sql = sql + " GROUP BY 1,2,3,4,5,6, 7, 8 "
    my_query = query_db(sql)
   # json_output = json.dumps(my_query)
    return jsonify(my_query)


@app.route("/json/faixaetaria/<ano>")
def getFaixaEtaria(ano):
    if (ano == '2014'):
        my_query = query_db("SELECT " +
                            "CASE " +
                            "  WHEN CAST(idade AS INT)<19 THEN '1-ATE 18' " +
                            "  WHEN CAST(idade AS INT)>20 THEN '3-ACIMA 21' " +
                            "  ELSE '2-ENTRE 19-20' " +
                            "END  AS fx, COUNT(*) as quant " +
                            "FROM enem.enem_2014  " +
                            "GROUP BY 1 ORDER BY 1")
    else:
        if (ano == '2015' or ano == '2016'):
            my_query = query_db("SELECT " +
                                "CASE " +
                                "  WHEN CAST(nu_idade AS INT)<19 THEN '1-ATE 18' " +
                                "  WHEN CAST(nu_idade AS INT)>20 THEN '3-ACIMA 21' " +
                                "  ELSE '2-ENTRE 19-20' " +
                                "END  AS fx, COUNT(*) as quant " +
                                "FROM enem.enem_"+ano+"  " +
                                "GROUP BY 1 ORDER BY 1")

    # json_output = json.dumps(my_query)
    return jsonify(my_query)                         # json_output


def db():
    con = psycopg2.connect(host='localhost', database='rbe',
                           user='postgres', password='postgres')

    return con


def query_db(query):
    cur = db().cursor()
    cur.execute(query)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return r  # (r[0] if r else None)


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Content-Type', 'application/json' ) 

  return response

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=5005, threaded=True)