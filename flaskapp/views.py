"""
auth.py

Date: 08/12/2023

Programmer's name: Suren Tumasyan

Description: Renders the home page and displays user information

"""

from flask import Blueprint, render_template, session
from flask_login import current_user

from .db import db
from .modules.models.user_model import Users

views = Blueprint('views', __name__)

@views.route('/')
def home():
    """Renders the home page and displays user information.
    
    Returns:
        str: Rendered HTML template with user information or anonymous user if not logged in.
    """
    curr_user = Users.get_user_by_email(session.get('user'))
    print(curr_user)
    return render_template("index.html", user=curr_user)