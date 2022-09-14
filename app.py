# Libraries
from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask_jwt_extended import  JWTManager

# Moduls
from querys import Query
from loginApi import loginApi
from exhibitionApi import exhibitionApi

app = Flask(__name__)

# Config mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'museo'
app.config["JWT_SECRET_KEY"] = "TikkiX2"

# Inits
jwt = JWTManager(app)
mysql = MySQL(app)

# Routes to templates of testing
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

# APIs
app.register_blueprint(loginApi)
app.register_blueprint(exhibitionApi)

if __name__ == "__main__":
    app.run(debug=True)