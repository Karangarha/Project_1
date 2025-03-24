"""Blueprint for homepage-related routes."""

from flask import Blueprint, render_template, request
from application.database import Users

homepage = Blueprint("homepage", __name__, template_folder="./templates")

@homepage.route("/")
def home():
    """Render the homepage."""
    return render_template("homepage.html")

@homepage.route("/about")
def about():
    """Render the about page."""
    return render_template("about.html")

@homepage.route("/users", methods=["POST", "GET"])
def users():
    """Retrieve and display all users."""
    all_users = Users.all()
    return render_template("users.html", users=all_users)

@homepage.route("/user/<username>")
def user(username):
    """Retrieve and display user details."""
    user_name = Users.find_user_by_name(username)
    return render_template("user.html", username=user_name)
