from flask import Blueprint, render_template, request, redirect, session, flash, jsonify
from flask_login import current_user
from .db import db

auth = Blueprint('auth', __name__)
from .modules.models.user_model import Users
from .modules.models.product_model import Products

@auth.route('/login', methods=['GET','POST'])
def login():
    curr_user = Users.get_user_by_email(session.get('user'))
    #If none, that means the curr_user isnt logged in, so send them to login page
    if curr_user == None:
        if request.method == 'POST':
            email = request.form.get('email')  # Get the email from the form
            error = None

            if not email:
                error = 'Email required'
            
            if error is None:
                if len(Users.query.filter(Users.email == email).all()) != 0:  # Find the user by email in the database
                    session['user'] = email
                    curr_user = Users.query.filter(Users.email == session['user']).first() 
                    flash('Logged in successfully!', 'alert-success')
                    return redirect('/products')  # Redirect to products or any other appropriate route
                else:
                    error = 'Invalid email. User does not exist.'

            flash(error, 'alert-danger')
    #if they are already logged in, just send them to the products page
    else:
        return redirect('/products')

    return render_template("login.html", user = curr_user)
    
@auth.route('/logout')
def logout():
    session['user'] = None
    return redirect('/') #just sends them back to index

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    curr_user = Users.get_user_by_email(session.get('user'))
    print(curr_user)
    
    #If none, that means the curr_user isnt logged in, so send them to login page
    if curr_user == None:
        if request.method == 'POST':
            email = request.form.get('email') #get the email
            print(email)
            error = None

            if not email:
                error = 'Email required'
            
            if error is None:
                if len(Users.query.filter(Users.email == email).all()) == 0:
                    user = Users(email=email)
                    db.session.add(user)
                    db.session.commit()
                    flash('User registered successfully!', 'alert alert-success') # Display success message
                    return redirect('/login')
                else:
                    error = f"User {email} is already registered."
                                
            flash(error, 'alert-danger')
            
    #if they are already logged in, just send them to the products page
    else:
        return redirect('/products')
        

    return render_template("sign_up.html", user = curr_user)



@auth.route("/search", methods=['GET', 'POST'])
def search():
    curr_user = Users.get_user_by_email(session.get('user'))
    if curr_user == None:
        return redirect('/login')
    else:

        if request.method == 'POST':
            search_item = request.form.get('searched')
            print(search_item)

            if search_item:
                search_results = Products.query.filter(Products.name.like(f'%{search_item}%')).all()
                print(search_results)

                return render_template('search.html', search_results=search_results, user=curr_user, search_item = search_item)

        return render_template('search.html', results=[], user=curr_user, search_item = search_item)