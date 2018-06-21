from flask import Flask, make_response, jsonify, render_template
import psycopg2
import json

app = Flask(__name__)


@app.route("/rbe/atendimentos/<ano>/<mes>")
def getAtendimentos(ano, mes):
    sql =       "SELECT unidade, ano, mes, dia, munic || ' (' || uf || ')' AS munic, bairro,  codbairrogeo,                               "
    sql = sql + " sexo, sala, fx_etaria, fx_hora, t_classif, t_atend, UPPER(encerramento) AS encerramento, count(*) as quant                                                   "
    sql = sql + " FROM (                                                                                                                  "
    sql = sql + " select DISTINCT u.descricaoabreviada as unidade,                                                                        "
    sql = sql + " f.codpaciente, f.uf, f.nome AS munic, b.bairro, m.geo_ind as codbairrogeo,  f.sexo,                                     "
    sql = sql + " f.nomeinterno AS sala,                                                                                                   "
    sql = sql + " f.datanascimento, EXTRACT(YEAR FROM age(f.dataatendimento, f.datanascimento)) AS idade,                                  "
    sql = sql + " CASE WHEN EXTRACT(YEAR FROM age(f.dataatendimento, f.datanascimento)) <= 1 THEN 'A:(0 -  1) RECEM NASCIDO '              "
    sql = sql + "      WHEN EXTRACT(YEAR FROM age(f.dataatendimento, f.datanascimento)) <=11 THEN 'B:(1 - 11) INFANCIA '                   "
    sql = sql + " 	 WHEN EXTRACT(YEAR FROM age(f.dataatendimento, f.datanascimento)) <=17 THEN 'C:(12 -17) ADOLESCENCIA '                 "
    sql = sql + " 	 WHEN EXTRACT(YEAR FROM age(f.dataatendimento, f.datanascimento)) <=40 THEN 'D:(18 -40) JOVEM '                        "
    sql = sql + " 	 WHEN EXTRACT(YEAR FROM age(f.dataatendimento, f.datanascimento)) <=65 THEN 'E:(41 -65) ADULTO '                       "
    sql = sql + "      ELSE 'F:(+65) IDOSO '                                                                                               "
    sql = sql + " END AS fx_etaria,                                                                                                        "
    sql = sql + "  EXTRACT(YEAR FROM f.dataatendimento) as ano,                                                                            "
    sql = sql + "  EXTRACT(MONTH FROM f.dataatendimento) as mes,                                                                           "
    sql = sql + "  EXTRACT(DAY FROM f.dataatendimento) as dia,                                                                             "
    sql = sql + " CASE WHEN EXTRACT(HOUR FROM f.datacriacao) >= 7 AND EXTRACT(HOUR FROM f.datacriacao) <= 12  THEN 'A:(7 - 12h)'           "
    sql = sql + "  WHEN EXTRACT(HOUR FROM f.datacriacao) >= 13 AND EXTRACT(HOUR FROM f.datacriacao) <= 19 THEN 'B:(13 - 19h)'              " 
    sql = sql + "  WHEN EXTRACT(HOUR FROM f.datacriacao) >= 20 AND EXTRACT(HOUR FROM f.datacriacao) <= 23 THEN 'C:(20 - 23h)'              "
    sql = sql + "  WHEN EXTRACT(HOUR FROM f.datacriacao) >= 00 AND EXTRACT(HOUR FROM f.datacriacao) <= 6  THEN 'D:(0h - 6h)'               "    
    sql = sql + "  ELSE 'E:(??)  '                                                                "                           
    sql = sql + " END AS fx_hora,     		                                                      "  
    sql = sql + " CASE WHEN minutos(i.datafimavaliacao, i.datacriacao) <= 5 THEN 'A - 5m'     "
    sql = sql + "     WHEN minutos(i.datafimavaliacao, i.datacriacao) <= 15 THEN 'B - 15m'    "
    sql = sql + "	 WHEN minutos(i.datafimavaliacao, i.datacriacao) <= 30 THEN 'C -  30m'     "
    sql = sql + "	 WHEN minutos(i.datafimavaliacao, i.datacriacao) <= 60 THEN 'D -  1h'      "
    sql = sql + "	 ELSE 'E - 2h ou +'                                                           "  
    sql = sql + " END AS t_classif,	                                                  "  
    sql = sql + " CASE WHEN minutos(f.datafimatendimento, f.datacriacao) <= 15 THEN 'A - 15m' "
    sql = sql + "      WHEN minutos(f.datafimatendimento, f.datacriacao) <= 60 THEN 'B - 1h'       " 
    sql = sql + "      WHEN minutos(f.datafimatendimento, f.datacriacao) <= 3*60 THEN 'C - 3h'     "
    sql = sql + "      WHEN minutos(f.datafimatendimento, f.datacriacao) <= 6*60 THEN 'D - 6h'     "
    sql = sql + "      WHEN minutos(f.datafimatendimento, f.datacriacao) <= 24*60 THEN 'E - 24h'   "
    sql = sql + "      ELSE 'F - 1 dia ou +'                                                           " 
    sql = sql + " END AS t_atend ,	                                                           "
    sql = sql + " CASE WHEN position('alta m' IN  LOWER(TRIM(f.descricaomotivo))) != 0     "
    # sql = sql + " 	       OR position('alta medica' IN  LOWER(TRIM(f.descricaomotivo))) != 0   "
    sql = sql + " 	           THEN 'Alta'                                                      "
    sql = sql + " 	   WHEN    position('encaminh' IN  LOWER(TRIM(f.descricaomotivo))) != 0     "
    sql = sql + " 	       OR  position('transfer' IN  LOWER(TRIM(f.descricaomotivo))) != 0     "
    sql = sql + " 		   OR  position('refer' IN  LOWER(TRIM(f.descricaomotivo))) != 0        "
    sql = sql + " 	           THEN 'Transferencia'                                             "
    sql = sql + " 	   WHEN    position('bito' IN  LOWER(TRIM(f.descricaomotivo))) != 0        "
    # sql = sql + " 	       OR  position('obito' IN  LOWER(TRIM(f.descricaomotivo))) != 0 		"  
    sql = sql + " 		       THEN 'Obito'                                                     "
    sql = sql + " 	   WHEN  LOWER(TRIM(f.motivoencerramento)) = 'outros' OR LENGTH(TRIM(f.descricaomotivo)) = 0 THEN 'Outros'  "
    sql = sql + " 	   WHEN LOWER(TRIM(f.motivoencerramento)) = 'alta' OR LOWER(TRIM(f.motivoencerramento)) = 'alta administrativa' THEN f.motivoencerramento "
    sql = sql + " 	   ELSE f.descricaomotivo                                                   "
    sql = sql + " 	END AS encerramento "
    sql = sql + " from dbo.pas_filaatendimento AS f                                                                                        "
    sql = sql + " left join dbo.pas_unidade as u on f.cnes = u.cnes                                                                        "
    sql = sql + " left join dbo.bairros as b on f.codbairro = b.codbairro                                                                  "
    sql = sql + " left join dbo.bairro_map as m on b.codbairro = m.codbairro 													           "
    sql = sql + " left join dbo.pas_avaliacaoinicial as i on f.codavaliacaoinicial = i.codavaliacaoinicial                                 "
    sql = sql + "  where                                                                                                                   "
    sql = sql + "   EXTRACT(YEAR FROM f.dataatendimento) = "  + ano
    sql = sql + "   AND EXTRACT(MONTH FROM f.dataatendimento) = " + mes
    sql = sql + "   AND f.dataexclusao IS NULL                                                                                             "
    sql = sql + "   AND f.nomeinterno IN ('ClinicoGeral', 'Odontologia', 'Pediatria', 'Traumatologia', 'Urgencia')        "
    sql = sql + "  ) AS tp                                                                                                                 "
    sql = sql + " GROUP BY 1,2,3,4,5,6, 7, 8, 9,10,11,12,13,14                                                                               "
    my_query = query_db(sql)
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