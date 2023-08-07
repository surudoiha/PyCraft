from flask import Blueprint, render_template, session
from flask_login import current_user

from .db import db
from .modules.models.user_model import Users

views = Blueprint('views', __name__)

@views.route('/')
def home():
    curr_user = Users.get_user_by_email(session.get('user'))
    print(curr_user)
    return render_template("index.html", user=curr_user)