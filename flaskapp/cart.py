from flask import Blueprint, render_template, session, redirect, url_for
from flask_login import current_user
from flask import flash

from .db import db
from .modules.models.user_model import Users
from .modules.models.cart_model import Cart

cart_blueprint = Blueprint('cart', __name__)

@cart_blueprint.route("/cart")
def cart():
    curr_user = Users.get_user_by_email(session.get('user'))
    if curr_user == None:
        return redirect('/login')
    else:
        cart_items = curr_user.get_user_cart()
        return render_template("cart.html", cart_items=cart_items, user=curr_user)