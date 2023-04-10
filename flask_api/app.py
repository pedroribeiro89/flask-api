from flask import Flask, make_response, jsonify, request

from flask_api.fake_bd import user_data
from flask_api.services.create_user_service import create_user_service
from flask_api.services.list_users_service import list_user_service

# from fake_bd import user_data

app = Flask(__name__)


@app.route("/users", methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        new_user_json = request.json
        return create_user_service(new_user_json)
    elif request.method == 'GET':
        return list_user_service()


