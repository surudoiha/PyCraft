"""
Module name: cart.py
Date:  08/04/2023
Programmer's name: Jorge Torrez and Ronny Almahdi

Description:
This module is responsible for handling cart-related operations in the e-commerce application. 
It includes routes for viewing the cart, updating cart items, and removing items from the cart.

Important data structure:
- Users and Cart models are utilized for querying and manipulating cart-related data in the database.

Algorithms:
- The update_cart() function uses a basic input validation to check if the user has provided a new quantity. 
- The remove_item() function deletes a cart item from the database based on the provided cart_id.
"""
from flask import Blueprint, render_template, session, redirect, url_for, request
from flask_login import current_user
from flask import flash

from .db import db
from .modules.models.user_model import Users
from .modules.models.cart_model import Cart

cart_blueprint = Blueprint('cart', __name__)

@cart_blueprint.route("/cart")
def cart():
    """
    Function:
    cart():
    - Description: Fetches and displays the cart items for the logged-in user.
    - Input: None
    - Output: Redirects the user to the login page if not logged in, otherwise renders the cart page.
    """
    curr_user = Users.get_user_by_email(session.get('user'))
    if curr_user == None:
        return redirect('/login')
    else:
        cart_items = curr_user.get_user_cart()
        return render_template("cart.html", cart_items=cart_items, user=curr_user)
    
@cart_blueprint.route("/update_cart/<int:cart_id>", methods=['GET', 'POST']) #the int will be the cart_id
def update_cart(cart_id):
    """
    Function:
    update_cart(cart_id:):
     - Description: Allows the user to update the quantity of a specific item in their cart. 
    - Input: cart_id (integer) which represents the ID of the cart item to be updated.
    - Output: Renders the update_cart template or redirects to the cart page after updating the quantity.
    """
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
    """
    remove_item(cart_id:):
    - Description: Allows the user to remove a specific item from their cart.
    - Input: cart_id (integer) which represents the ID of the cart item to be removed.
    - Output: Redirects the user to the cart page after removing the item.
    """
    curr_user = Users.get_user_by_email(session.get('user'))
    if curr_user == None:
        return redirect('/login')
    else:
        Cart.remove_item(cart_id)
        flash("Successfully Removed Item", "alert-success")
        
    return redirect('/cart')
