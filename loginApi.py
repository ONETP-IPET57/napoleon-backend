# Libraries
from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, jsonify
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required, set_access_cookies, unset_jwt_cookies
import hashlib

# Moduls
from querys import Query
from main import jwt

# Init router
loginApi = Blueprint('loginApi', __name__, template_folder='app/templates')

# Routes of Login APIs

# Login Route
@loginApi.route("/api/login", methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        userData= Query.fetch_user_login(username, password)
        if userData != None:
            
            access_token = create_access_token(identity={
                'id_user': userData[0],
                'username': userData[1],
                'email': userData[3],
                'role': userData[4],
            })

            response = jsonify({
                    'accessToken': access_token,
                    'username': userData[0],
                    'email': userData[2],
                    'role': userData[3],
                })
            set_access_cookies(response, access_token)
            return response
        else:
            return jsonify({
                "message": "User not found!" 
            }), 401


# token in cookies
@loginApi.route("/api/user", methods=['GET'])
@jwt_required(locations=['cookies','headers'])
def user():
    current_user = get_jwt_identity()
    return jsonify(current_user), 200

# SignUp Route
@loginApi.route("/api/signup", methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.json.get("username", None)
        email = request.json.get("email", None)
        password = request.json.get("password", None)
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if Query.fetch_user_signup(username=username, email=None):
            if Query.fetch_user_signup(username=None, email=email):
                userData= Query.insert_user(username,password,email)
                
                print(userData)
                access_token = create_access_token(identity={
                    'id_user': userData[0],
                    'username': userData[1],
                    'email': userData[3],
                    'role': userData[4],
                })

                response = jsonify({
                    'accessToken': access_token,
                    'username': userData[1],
                    'email': userData[3],
                    'role': userData[4],
                })

                set_access_cookies(response, access_token)
                return response

            else:
                return jsonify({
                "message": "Your email is registered"
            }), 401
        else:
            return jsonify({
                "message": "Your username is registered"
            }), 401

# Logout Route
@loginApi.route("/api/logout", methods=['POST'])
def logout():
    response = jsonify({"message": "Logout Successful"})
    unset_jwt_cookies(response)
    return response