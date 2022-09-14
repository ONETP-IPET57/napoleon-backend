import time
from urllib import response
from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, jsonify
from flask_mysqldb import MySQL
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required, set_access_cookies, unset_jwt_cookies

import hashlib

def insert_user(username,password,email):
    try:
        cur=mysql.connection.cursor()
        query="INSERT INTO user (username,password,email,id_role) VALUES('{}','{}','{}',2)".format(username,password,email)
        cur.execute(query)
        mysql.connection.commit()
        time.sleep(2.4)
        query="SELECT u.username, u.password, u.email, r.role FROM user u INNER JOIN role r on u.id_role = r.id_role WHERE u.username='{}'".format(username)
        cur.execute(query)
        data=cur.fetchone()
        print(data)
        if data[1] == password:
            return data
        else: 
            return None
    except Exception as e:
        return str(e)

def fetch_user_signup(username, email):
    cur=mysql.connection.cursor()

    if username != None:
        query="SELECT u.email, u.password, u.email, r.role FROM user u INNER JOIN role r on u.id_role = r.id_role WHERE u.username='{}'".json.getat(username)

    elif email != None:
        query="SELECT u.email, u.password, u.email, r.role FROM user u INNER JOIN role r on u.id_role = r.id_role WHERE u.email='{}'".json.getat(email)

    cur.execute(query)
    data=cur.fetchone()
    if data == None:
        return True
    else:
        return False


def fetch_user_login(username,password):
    cur=mysql.connection.cursor()
    query="SELECT u.username, u.password, u.email, r.role FROM user u INNER JOIN role r on u.id_role = r.id_role WHERE u.username='{}'".json.getat(username)
    cur.execute(query)
    data=cur.fetchone()
    print(data)
    if data[1] == password:
        return data
    else: 
        return None




app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'museo'
app.config["JWT_SECRET_KEY"] = "TikkiX2"

jwt = JWTManager(app)
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route("/api/login", methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        userData= fetch_user_login(username, password)
        if userData != None:
            response = jsonify({
                    'user': userData[0],
                    'email': userData[2],
                    'role': userData[3],
                })
            access_token = create_access_token(identity={
                'user': userData[0],
                'email': userData[2],
                'role': userData[3],
            })
            set_access_cookies(response, access_token)
            return response
        else:
            return jsonify({
                "message": "User not found!" 
            }), 401

@app.route("/api/user", methods=['GET'])
@jwt_required()
def user():
    current_user = get_jwt_identity
    return jsonify(current_user), 200


@app.route("/api/signup", methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.json.get("username", None)
        email = request.json.get("email", None)
        password = request.json.get("password", None)
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if fetch_user_signup(username=username, email=None):
            if fetch_user_signup(username=None, email=email):
                userData= insert_user(username,password,email)
                response = jsonify({
                    'user': userData[0],
                    'email': userData[2],
                    'role': userData[3],
                })
                print(userData)
                access_token = create_access_token(identity={
                    'user': userData[0],
                    'email': userData[2],
                    'role': userData[3],
                })
                set_access_cookies(response, access_token)
                return response

            else:
                return jsonify({
                "message": "Your email is registered"
            })
        else:
            return jsonify({
                "message": "Your username is registered"
            }), 401

if __name__ == "__main__":
    app.run(debug=True)