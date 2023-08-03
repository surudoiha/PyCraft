from flask import Blueprint, render_template, session
from flask_login import current_user

from .db import db, Users, Cart

views = Blueprint('views', __name__)

@views.route('/')
def home():
    curr_user = Users.query.filter(Users.email == session['user']).first() 
    print(curr_user)
    return render_template("index.html", user=curr_user)