from flask import Blueprint, render_template
from flask_login import current_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    #user = current_user
    return render_template("login.html", user=current_user)
    
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    #user = current_user
    return render_template("sign_up.html", user=current_user)