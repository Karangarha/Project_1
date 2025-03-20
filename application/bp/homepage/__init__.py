from flask import Blueprint, render_template,request

from application.database import Users

homepage = Blueprint('homepage', __name__, template_folder='./templates')

@homepage.route('/')
def home():
    return render_template("homepage.html")

@homepage.route('/about')
def about():
    return render_template("about.html")

@homepage.route('/users', methods = ['POST','GET'])
def users():
    all_users = Users.all()
    return render_template("users.html", users=all_users)

@homepage.route('/user/<username>')
def user(username):
    user_name=Users.find_user_by_name(username)
    return render_template("user.html", username=user_name )