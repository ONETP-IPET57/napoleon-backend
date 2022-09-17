from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, jsonify
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required, set_access_cookies, unset_jwt_cookies
import hashlib
import randomname

# Moduls
from querys import Query
from main import jwt

# Init router
visitsApi = Blueprint('visitsApi', __name__, template_folder='app/templates')

@visitsApi.route('/api/guided_tours', methods=['GET'])
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

@visitsApi.route('/api/guided_tours/<id>', methods=['GET'])
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

@visitsApi.route('/api/visit/<id>', methods=['POST','DELETE'])
@jwt_required(locations='cookies')
def visit(id):
    id_user = get_jwt_identity()['id_user']
    if id_user == None:
        return jsonify({'message': 'Not user logged'}), 403

    if request.method == 'POST':
        id_guided_tours = request.json.get('id_guided_tours', None)
        reference_name = randomname.get_name()
        return jsonify(Query.insert_visit(id_guided_tours, id_user, reference_name)), 200

    if request.method == 'DELETE':
        return jsonify(Query.delete_visit(id))

@visitsApi.route('/api/user/visits', methods=['GET'])
@jwt_required(locations='cookies')
def user_visits():
    id_user = get_jwt_identity()['id_user']
    if id_user == None:
        return jsonify({'message': 'Not user logged'}), 403

    if request.method == 'GET':
        dataUserVisit = Query.fetch_all_visit(id_user)
        jsonUserVisit = []

        for data in dataUserVisit:
            jsonUserVisit.append({
                'id_visit': data[0],
                'name_guided_tours': data[1],
                'description': data[2],
                'reference_name': data[3]
            })

    return jsonify(jsonUserVisit)