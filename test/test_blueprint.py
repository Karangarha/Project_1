"""Test module for blueprint registration in Flask application."""

from application import init_app

def test_bp_usage():
    """Test if there is a blueprint registered."""
    assert init_app().blueprints.keys(), "No Blueprint Registered!"
