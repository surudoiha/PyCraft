from flask import Blueprint, render_template, request, redirect, session, flash
from flask_login import current_user
from .db import db, Users, Cart

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')  # Get the email from the form
        error = None

        if not email:
            error = 'Email required'
        
        if error is None:
            if len(Users.query.filter(Users.email == email).all()) != 0:  # Find the user by email in the database
                user = Users.query.filter(Users.email == email).first()
                session['user_id'] = user.id
                flash('Logged in successfully!')
                return redirect('/products')  # Redirect to products or any other appropriate route
            else:
                error = 'Invalid email. User does not exist.'

        flash(error)

    return render_template("login.html")
    
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')                        #get the email
        print(email)
        error = None

        if not email:
            error = 'Email required'
        
        if error is None:
            if len(Users.query.filter(Users.email == email).all()) == 0:
                user = Users(email=email)
                db.session.add(user)
                db.session.commit()
                flash('User registered successfully!')               # Display success message
                return redirect('/login')
            else:
                error = f"User {email} is already registered."
                            

        flash(error)

    return render_template("sign_up.html")