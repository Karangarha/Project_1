import pytest
from application import init_app

def test_bp_usage():
    """Test if there is blueprint registered"""
    assert init_app().blueprints.keys(), "No Blueprint Registered!"