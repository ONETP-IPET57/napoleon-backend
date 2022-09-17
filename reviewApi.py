# Libraries
from flask import  request, Blueprint, jsonify
from flask_jwt_extended import  get_jwt_identity, jwt_required

# Moduls
from querys import Query
from main import jwt

reviewApi = Blueprint('reviewApi', __name__, template_folder='app/templates')

@reviewApi.route('/api/reviews/', methods=['GET','POST'])
@jwt_required(locations='cookies')
def reviews(id):
    id_user = get_jwt_identity()['id_user']
    if id_user == None:
        return jsonify({'message': 'Not user logged'}), 403

    if request.method == 'GET':
        dataExhibition = Query.fetch_exhibition(id)
        dataReviews = Query.fetch_all_review()

        jsonReviews = []

        for data in dataReviews:
            jsonReviews.append({
                'id_user': data[0],
                'username': data[1],
                'score': data[2],
                'message': data[3]
            })

        return jsonify([jsonReviews, dataExhibition])

    if request.method == 'POST':
        score = request.json.get('score', None)
        message = request.json.get('message', None)
        return jsonify(Query.insert_review(id,id_user,score,message))

@reviewApi.route('/api/reviews/<id>', methods=['POST','DELETE'])
def review(id):
    if request.method == 'POST':
        score = request.json.get('score', None)
        message = request.json.get('message', None)
        return Query.update_review(score, message, id)

    if request.method == 'DELETE':
        return jsonify(Query.delete_review(id))
