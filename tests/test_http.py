import pytest
import requests

@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print ("Response is {}".format(r.text))

@pytest.mark.http
def test_second_request():
    r = requests.get(' https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['type'] == "User"
    assert headers['Server'] == 'github.com'
    assert r.status_code == 200

@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko ')
    assert r.status_code == 404


