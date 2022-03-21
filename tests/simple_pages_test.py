"""This test the homepage"""


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index Page" in response.data


def test_request_git_page(client):
    """This makes the git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data


def test_request_docker_page(client):
    """This makes the docker page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data


def test_request_flask_page(client):
    """This makes the flask page"""
    response = client.get("/flask")
    assert response.status_code == 200
    assert b"Flask" in response.data


def test_request_cicd_page(client):
    """This makes the CICD page"""
    response = client.get("/CICD")
    assert response.status_code == 200
    assert b"CI/CD" in response.data
