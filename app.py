import randomname
from flask import Flask, render_template, jsonify,request
from flask_mysqldb import MySQL
from flask_jwt_extended import  JWTManager, jwt_required, get_jwt_identity

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

@app.route('/api/guided_tours', methods=['GET'])
def guided_tours():
    if request.method == 'GET':
        toursData = Query.fetch_all_guided_tours()
        jsonGuidedTour = []

        for tour in toursData:
            jsonGuidedTour.append({
            'id_guided_tours': tour[0],
            'name_guided_tours': tour[1],
            'description': tour[2],
            'hour_start': str(tour[3]),
            'hour_end': str(tour[4]),
            'day': tour[5]
        })
        return jsonify(jsonGuidedTour)

@app.route('/api/guided_tours/<id>', methods=['GET'])
def guided_tour(id):
    if request.method == 'GET':
        tourDate = Query.fetch_guided_tour(id)

        return jsonify({
            'id_guided_tours': tourDate[0],
            'name_guided_tours': tourDate[1],
            'description': tourDate[2],
            'hour_start': str(tourDate[3]),
            'hour_end': str(tourDate[4]),
            'day': tourDate[5]
        })

@app.route('/api/visit', methods=['POST','DELETE'])
@jwt_required(locations='cookies')
def visit():
    id_user = get_jwt_identity()['id_user']
    if id_user == None:
        return jsonify({'message': 'Not user logged'}), 403

    if request.method == 'POST':
        id_guided_tours = request.json.get('id_guided_tours', None)
        date = request.json.get('date', None)
        reference_name = randomname.get_name()
        return jsonify(Query.insert_visit(id_guided_tours, id_user, date, reference_name)), 200

    if request.method == 'DELETE':
        return jsonify(Query.delete_visit)

@app.route('/api/user/visits', methods=['GET'])
@jwt_required(locations='cookies')
def user_visits():
    id_user = get_jwt_identity()['id_user']
    if id_user == None:
        return jsonify({'message': 'Not user logged'}), 403

    if request.method == 'GET':
        dataUserVisit = Query.fetch_all_visit()
        jsonUserVisit = []

        for data in dataUserVisit:
            jsonUserVisit.append({
                'name_guided_tours': data[0],
                'description': data[1],
                'reference_name': data[2]
            })

    return jsonify(jsonUserVisit)


        
# APIs
app.register_blueprint(loginApi)
app.register_blueprint(exhibitionApi)

if __name__ == "__main__":
    app.run(debug=True)