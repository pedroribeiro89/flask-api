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


def test_add_user():
    expected_id = -1
    for db_user in user_data:
        if db_user['id'] > expected_id:
            expected_id = db_user['id']

    data = {
        "name": "Pedro Soares",
        "phone": "(31) 99999-9999",
        "email": "psoares@teste.com",
        "country": "Brazil"
    }
    response = api.test_client().post('/users', json=data)
    print(response)
    user = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert user['name'] == 'Pedro Soares'
    assert user['phone'] == '(31) 99999-9999'
    assert user['email'] == 'psoares@teste.com'
    assert user['country'] == 'Brazil'
    assert user['id'] == expected_id + 1

