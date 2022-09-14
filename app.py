from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, jsonify
from flask_jwt_extended import  JWTManager
from flask_mysqldb import MySQL
from querys import Query
from loginApi import loginApi

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'museo'

app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
app.config["JWT_COOKIE_SECURE"] = False

app.config["JWT_SECRET_KEY"] = "TikkiX2"


jwt = JWTManager(app)
mysql = MySQL(app)

@app.route('/')
def index():
    datas=Query.fechtAllUsers()
    return render_template('index.html', datas=datas)

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

app.register_blueprint(loginApi)

if __name__ == "__main__":
    app.run(debug=True)