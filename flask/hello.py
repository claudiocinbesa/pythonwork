from flask import Flask, make_response, jsonify, render_template 
# #   
# # from flask_excel   from flask.ext import excel 
import json
pessoas = [{"nome": "Bruno Rocha"},
               {"nome": "Arjen Lucassen"},
               {"nome": "Anneke van Giersbergen"},
               {"nome": "Steven Wilson"}]
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/html_page/<nome>")
def html_page(nome):
    return render_template("html_page.html", nome=nome)

@app.route("/temp/<string:input>") 
def temp(input):
    if input=='all':
        resp = json.dumps(pessoas), 200, {"Content-Type": "application/json"}
    else:
        resp = "<h1>Teste de Flask no Python</h1> <BR> PARAM = " + input
    return resp

@app.route("/json_api1/")
def json_api1():
     
    return json.dumps(pessoas), 200, {"Content-Type": "application/json"}

@app.route("/json_api2/")
def json_api2():
    return jsonify(pessoas=pessoas, total=len(pessoas))

@app.route("/json_api3/")
def json_api3():
    response = make_response(json.dumps(pessoas))
    response.content_type = "application/json"
    # ou
    # response.headers['Content-Type'] = "application/json"
    return response


@app.route('/csv/', methods=['GET', 'POST'])  
def download_csv():  
    csv = 'foo,bar,baz\nhai,bai,crai\n'  
    response = make_response(csv)
    cd = 'attachment; filename=mycsv.csv'
    response.headers['Content-Disposition'] = cd 
    response.mimetype='text/csv'

    return response

@app.route('/downloadcsv/')
def downloadcsv():
    data = [
        ["REVIEW_DATE","AUTHOR","ISBN","DISCOUNTED_PRICE"],
        ["1985/01/21","Douglas Adams",'0345391802',5.95],
        ["1990/01/12","Douglas Hofstadter",'0465026567',9.95],
        ["1998/07/15","Timothy \"The Parser\" Campbell",'0968411304',18.99],
        ["1999/12/03","Richard Friedman",'0060630353',5.95],
        ["2004/10/04","Randel Helms",'0879755725',4.50]
    ]
    # output = excel.make_response_from_array(data, 'csv')
    # output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    # output.headers["Content-type"] = "text/csv"
    # return output
    # response = make_response(excel.make_response_from_array(data, 'csv'))
    response = make_response(data)
    cd = 'attachment; filename=mycsv.csv'
    response.headers['Content-Disposition'] = cd 
    response.mimetype='text/csv'
    return  response 
   
if __name__ == "__main__": 
    app.run(debug=True)
