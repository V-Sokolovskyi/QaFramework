import pytest



@pytest.mark.api
@pytest.mark.user
def test_user_exists(github_api):
    """

    Test if an existing GitHub user can be retrieved.

    """
    user = github_api.get_user("defunkt")
    assert user['login'] == 'defunkt', "The login name does not match the expected value."

@pytest.mark.api
@pytest.mark.user
def test_user_not_exists(github_api):
    """

    Test for handling non-existent GitHub users.

    """
    r = github_api.get_user("Not Found")
    assert r["message"] == "Not Found", "The API did not return the expected error message."

@pytest.mark.api
@pytest.mark.repo
def test_repo_exists(github_api):
    repo = github_api.get_repositories("qafram", 70)
    """
    Test if a repository exists in the search results.

    """
    
    if repo["items"][0]["name"] == "openmrs-contrib-qaframework":
        print(f"The first of list of {repo['total_count']} repositories")
    else:
        index = next(i for i, r in enumerate(repo["items"]) if r["name"] == "openmrs-contrib-qaframework") 
        print(f"Repo found, number of first repo in the same name in list is {index + 1}")

@pytest.mark.api
@pytest.mark.repo
def test_repo_non_exists(github_api):
    """
    Test for handling a repository search with no results.

    """
    repo = github_api.get_repositories("xdvbdfghdfg", 70)
    assert repo["total_count"] == 0, "The search returned results when none were expected."

@pytest.mark.api
@pytest.mark.repo
def test_repo_no_name(github_api):
    """
    Test for handling a repository search with no name provided.

    """
    repo = github_api.get_repositories_no_name("", 20)
    assert repo.status_code == 422, "The API did not return the expected 422 status code for empty query."


@pytest.mark.api
@pytest.mark.create
def test_repo_crate(github_api):
    """
    Test for creating a new GitHub repository.

    """
    repo = github_api.create_repo("new_repo")
    body  = repo.json()

    assert repo.status_code == 201, "Failed to create a new repository."
    assert body["name"] == "new_repo", "Repository name does not match."
    assert body["private"] == False, "Repository privacy setting is incorrect."
  
@pytest.mark.api
@pytest.mark.delete
def test_repo_delete(github_api):
    """

    Test for deleting an existing GitHub repository.

    """
    repo =github_api.delete_repo("new_repo")
    assert repo.status_code == 204, "Failed to delete the repository."

@pytest.mark.api
@pytest.mark.misc
def test_get_emojis(github_api):
    """

    Test for retrieving GitHub emojis.

    """
    emojis = github_api.get_emojis()
    airpalne = "https://github.githubassets.com/images/icons/emoji/unicode/2708.png?v8"
    assert emojis.json()["airplane"] == airpalne, "The airplane emoji URL does not match the expected value."
   


@pytest.mark.api
@pytest.mark.update
def test_update_data(github_api):
    """
    Test for updating repository data (e.g., description).

    """
    r =github_api.updare_repo("api-test-akaunt", "new_repo", "new descript" )

    assert r.status_code == 200, "Failed to update repository data."
