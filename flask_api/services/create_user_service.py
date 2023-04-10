from flask import make_response, jsonify

from flask_api.fake_bd import user_data


def create_user_service(new_user_json):
    max_id = 0
    for user in user_data:
        if user['id'] > max_id:
            max_id = user['id']
    new_user = {'id': max_id + 1,
                'name': new_user_json['name'],
                'phone': new_user_json['phone'],
                'email': new_user_json['email'],
                'country': new_user_json['country']}
    user_data.append(new_user)
    return make_response(
        jsonify(new_user)
    )
