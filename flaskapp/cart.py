from flask import Blueprint, render_template, session, redirect, url_for, request
from flask_login import current_user
from flask import flash

from .db import db
from .modules.models.user_model import Users
from .modules.models.cart_model import Cart
from .modules.models.product_model import Products

cart_blueprint = Blueprint('cart', __name__)

@cart_blueprint.route("/cart")
def cart():
    curr_user = Users.get_user_by_email(session.get('user'))
    if curr_user == None:
        return redirect('/login')
    else:
        cart_items = curr_user.get_user_cart()
        return render_template("cart.html", cart_items=cart_items, user=curr_user, products = Products.get_prod_list())
    
@cart_blueprint.route("/update_cart/<int:cart_id>", methods=['GET', 'POST']) #the int will be the cart_id
def update_cart(cart_id):
    curr_user = Users.get_user_by_email(session.get('user'))
    if curr_user == None:
        return redirect('/login')
    else:
        if request.method == "POST":
            cart_item_to_change = Cart.query.filter(Cart.cart_id == cart_id).first()
            new_quantity = request.form.get('quantity')
            error = None
            
            if not new_quantity:
                error = "you need to input a number"
            
            if error is None:
                
                print(type(new_quantity))
                Cart.update_cart_quantity(curr_user, cart_item_to_change, new_quantity)
                flash("Successfully Updated Item", "alert-warning")
                return redirect('/cart')

    return render_template("update_cart.html", prod_to_change=cart_item_to_change, user=curr_user)
    
@cart_blueprint.route("/cart/remove_item/<int:cart_id>", methods=['GET', 'POST'])
def remove_item(cart_id):
    curr_user = Users.get_user_by_email(session.get('user'))
    if curr_user == None:
        return redirect('/login')
    else:
        Cart.remove_item(cart_id)
        flash("Successfully Removed Item", "alert-success")
        
    return redirect('/cart')
