from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, jsonify
from flask_mysqldb import MySQL
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required, set_access_cookies, unset_jwt_cookies

from querys import Query
from loginApi import loginApi
import hashlib

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
    datas = Query.fechtAllUsers()
    return render_template('index.html', datas=datas)

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/api/exhibitions', methods=['GET'])
def exhibitions():
    if request.method == 'GET':
        dataExhibitions = Query.fetch_all_exhibition()
        jsonExhibitions = []

        for data in dataExhibitions:
            jsonExhibitions.append({
                'id_exhibition': data[0],
                'name_exhibition': data[1],
                'author': data[2],
                'created_at': data[3],
                'information': data[4],
                'image': data[5]
            })
        return jsonify(jsonExhibitions)

@app.route('/api/exhibition/<id>', methods=['POST','GET','DELETE'])
@jwt_required(locations='cookies')
def exhibition(id):
    if get_jwt_identity().role != 'administrator':
        return jsonify({'message': 'Not authorized'}), 403

    if request.method == 'GET':
        dataExhibition = Query.fetch_exhibition(id)
        return jsonify({
            'id_exhibition': dataExhibition[0],
            'name_exhibition': dataExhibition[1],
            'author': dataExhibition[2],
            'created_at': dataExhibition[3],
            'information': dataExhibition[4],
            'image': dataExhibition[5]
        })
    
    if request.method == 'DELETE':
        return jsonify(Query.delete_exhibition(id))
    
    if request.method == 'POST':
        id_exhibition = id
        name_exhibition = request.json.get("name_exhibition", None)
        author = request.json.get("author", None)
        created_at = request.json.get("created_at", None)
        information = request.json.get("information", None)
        image = request.json.get("image", None)

        return jsonify(Query.update_exhibition(id_exhibition,name_exhibition, author, created_at, information, image))


app.register_blueprint(loginApi)

if __name__ == "__main__":
    app.run(debug=True)