from flask import Flask
from flask_mysqldb import MySQL


def prueba():
    cur = mysql.connection.cursor()
    query = "SELECT * FROM user"
    cur.execute(query)
    data = cur.fetchone()
    return str(data)

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'museo'

@app.route('/')
def index():
    return prueba()

if __name__ == "__main__":
    app.run(debug=False)