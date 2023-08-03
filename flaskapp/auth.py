<<<<<<< Updated upstream
from flask import Blueprint, render_template, request, redirect, session, flash
=======
from flask import Blueprint, render_template, request, redirect, flash, session
>>>>>>> Stashed changes
from flask_login import current_user
from .db import db, Users, Cart

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
<<<<<<< Updated upstream
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
=======
    curr_user = Users.query.filter(Users.email == session['user']).first()
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
>>>>>>> Stashed changes
    
@auth.route('/logout')
def logout():
    session['user'] = None
    #return redirect('/') #just sends them back to index
    return "<p>Logout</p>"

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
<<<<<<< Updated upstream
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
=======
    curr_user = Users.query.filter(Users.email == session['user']).first() 
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
>>>>>>> Stashed changes
