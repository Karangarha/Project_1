"""Test module for Flask application routes and content."""

import pytest
from application import init_app

@pytest.fixture(name="client")
def create_client():
    """Initialize a fixture test client for Flask unit testing."""
    with init_app().test_client() as app_client:
        yield app_client

def test_main_page_content(client):
    """Flask unit testing for content on the default page."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"My IS601" in response.data

def test_about_page_content(client):
    """Flask unit testing for content on the about page."""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"about" in response.data

def test_users_page(client):
    """Flask unit testing for the users page."""
    response = client.get("/users")
    assert response.status_code == 200
    assert b"Users" in response.data
