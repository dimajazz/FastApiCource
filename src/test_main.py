
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_all_blogs():
    response = client.get('/blog/all')
    assert response.status_code == 200


def test_auth_error():
    response = client.post('/token', data={'username': '', 'password': ''})
    access_token = response.json().get('access_token')
    assert access_token == None

    message = response.json().get('detail')[0].get('msg')
    assert message == 'Field required'


def test_auth_success():
    response = client.post(
        '/token', data={'username': 'testuser', 'password': 'testuser'})
    access_token = response.json().get('access_token')
    assert access_token


def test_post_article():
    auth = client.post(
        '/token', data={'username': 'testuser', 'password': 'testuser'})
    access_token = auth.json().get('access_token')

    assert access_token

    response = client.post(
        '/article/new',
        json={
            'title': 'Test article',
            'content': 'Test content',
            'published': True,
            'creator_id': 2
        },
        headers={
            'Authorization': 'bearer ' + access_token
        })

    assert response.status_code == 200
    assert response.json().get('title') == 'Test article'
