# Libraries
from flask import  request, Blueprint, jsonify
from flask_jwt_extended import  get_jwt_identity, jwt_required

# Moduls
from querys import Query
from main import jwt

# Init router
exhibitionApi = Blueprint('exhibitionApi', __name__, template_folder='app/templates')

# Routes of exhibitions APIs

# Fetch all exhibitions
@exhibitionApi.route('/api/exhibitions', methods=['GET'])
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
                'image': data[5],
                'beepcons': data[6]
            })
        return jsonify(jsonExhibitions)

# Fetch one exhibition for to work
@exhibitionApi.route('/api/exhibition/<id>', methods=['POST','GET','DELETE'])
@jwt_required(locations='cookies')
def exhibition(id):
    if get_jwt_identity()['role'] != 'administrator':
        return jsonify({'message': 'Not authorized'}), 403

    # Get one exhibition to the frontend
    if request.method == 'GET':
        dataExhibition = Query.fetch_exhibition(id)
        return jsonify({
            'id_exhibition': dataExhibition[0],
            'name_exhibition': dataExhibition[1],
            'author': dataExhibition[2],
            'created_at': dataExhibition[3],
            'information': dataExhibition[4],
            'image': dataExhibition[5],
            'beepcons': dataExhibition[6]
        })

    # Delete one exhibition from Database
    if request.method == 'DELETE':
        return jsonify(Query.delete_exhibition(id))

    # Edit one exhibition from Database
    if request.method == 'POST':
        id_exhibition = id
        name_exhibition = request.json.get("name_exhibition", None)
        author = request.json.get("author", None)
        created_at = request.json.get("created_at", None)
        information = request.json.get("information", None)
        image = request.json.get("image", None)
        beepcons = request.json.get("beepcons", None)

        return jsonify(Query.update_exhibition(id_exhibition,name_exhibition, author, created_at, information, image,beepcons))

# Get exhibition datas to add to the database
@exhibitionApi.route('/api/exhibition/add', methods=['POST'])
def exhibitionAdd():
    if request.method == 'POST':
        name_exhibition = request.json.get("name_exhibition", None)
        author = request.json.get("author", None)
        created_at = request.json.get("created_at", None)
        information = request.json.get("information", None)
        image = request.json.get("image", None)

        return jsonify(Query.insert_exhibition(name_exhibition, author, created_at, information, image))