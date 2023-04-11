import json
from flask_api.app import api
from flask_api.fake_bd import user_data


def test_list_users():
    """List users, should get all user from fake_db."""
    response = api.test_client().get('/users')
    listed_users = json.loads(response.data.decode('utf-8'))

    result = 0
    for user in user_data:
        for user_result in listed_users:
            if user['id'] == user_result['id']:
                result += 1

    expect = len(user_data)
    assert response.status_code == 200
    assert result == expect

