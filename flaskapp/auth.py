from flask import Blueprint, render_template, request
from flask_login import current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    #user = current_user
    return render_template("login.html", user=current_user)
    
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    #user = current_user
    if request.method == 'POST':
        email = request.form.get('inputEmail')

        #email handling temp version (sendigng to database, saving ...)
        #also redirecting to different page doesnt work after successful sign-up

        return render_template('products.html', email=email)

    return render_template("sign_up.html", user=current_user)