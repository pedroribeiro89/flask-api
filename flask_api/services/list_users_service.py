from flask import make_response, jsonify

from flask_api.fake_bd import user_data


def list_user_service():
    return make_response(
        jsonify(user_data)
    )

