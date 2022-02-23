"""This test the homepage"""


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/")
    assert b"Benchuan's First Bootstrap Site" in response.data

def test_request_example(client):
    """This makes the index page"""
    response = client.get("/about")
    assert b"Lorem ipsum dolor" in response.data
