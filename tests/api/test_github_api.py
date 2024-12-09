import pytest



@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("Not Found")
    assert r["message"] == "Not Found"
