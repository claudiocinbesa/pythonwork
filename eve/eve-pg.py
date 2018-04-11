from eve import Eve
from eve_sqlalchemy import SQL
app = Eve(data=SQL)

if __name__ == '__main__':
    app.run()