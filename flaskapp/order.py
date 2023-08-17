from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from flask_login import current_user
import requests

from .db import db
from .modules.models.user_model import Users
from .modules.models.order_model import Orders

orders_blueprint = Blueprint('orders', __name__)

@orders_blueprint.route("/orders") 
def checkout():
    curr_user = Users.get_user_by_email(session.get('user'))
    if curr_user == None:
        return redirect('/login')
    else:
        curr_user_email = "pycraft380@gmail.com"
        orders = Orders.query.filter(Orders.owner_id == curr_user.id).all()
        if orders:
            return render_template("order.html", user=curr_user, orders=orders)
        
            
    flash("You have no orders!", 'alert-danger')
    
    return redirect('/cart')

