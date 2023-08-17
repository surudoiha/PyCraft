"""
auth.py

Date: 08/12/2023

Programmer's name: Suren Tumasyan, Ronny Almahdi

Description: handles routes and authentification

"""

from flask import Blueprint, render_template, request, redirect, session, flash, jsonify
from flask_login import current_user
from .db import db

auth = Blueprint('auth', __name__)
from .modules.models.user_model import Users
from .modules.models.product_model import Products

@auth.route('/login', methods=['GET','POST'])
def login():
    """Handles user login process.
    
    If the user is not logged in, the function either displays the login form (GET request)
    or processes the submitted form data to authenticate and log in the user (POST request).
    If the user is already logged in, they are redirected to the products page.
    
    Returns:
        str: Rendered HTML template with the login form or appropriate messages.
        Redirect: Redirects to the products page if the user is already logged in.
    """
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
    """Logs out the user by clearing the session and redirects to the index page.
    
    Returns:
        redirect: Redirects the user to the index page.
    """
    session['user'] = None
    return redirect('/') #just sends them back to index

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    """Handles user sign-up process.
    
    If the user is not logged in, the function either displays the sign-up form (GET request)
    or processes the submitted form data to create a new user account (POST request).
    
    Returns:
        str: Rendered HTML template with the sign-up form or appropriate messages.
    """
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
    """Handles product search functionality.
    
    If the user is not logged in, redirects them to the login page. Otherwise, the function
    processes search requests (POST) and displays search results or the search form (GET).
    
    Returns:
        str: Rendered HTML template with search results or search form.
    """
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