from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
from flask_mysqldb import MySQL
import hashlib


def insert_user(username,password):
    try:
        cur=mysql.connection.cursor()
        query="INSERT INTO user (username,password) VALUES('{}','{}')".format(username,password)
        cur.execute(query)
        mysql.connection.commit()
        return redirect(url_for('index'))
    except Exception as e:
        return str(e)

def fetch_users():
    try:
        cur=mysql.connection.cursor()
        query="SELECT * FROM user"
        cur.execute(query)
        data=cur.fetchall()
        return data
    except Exception as e:
        return str(e)

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'museo'

app.secret_key = "mysecretkey"


@app.route('/')
def index():
    datas = fetch_users()
    return render_template('index.html', datas=datas)

if __name__ == "__main__":
    app.run(debug=True)