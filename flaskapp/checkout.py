"""
Module: checkout.py

Date: 08/12/2023

Programmer's Name: Jorge Torrez 

Description:
This module contains the blueprint and the associated route for the checkout page of the e-commerce website.
It manages the operations related to rendering the checkout page, calculating order totals, and verifying user authentication.

Data Structures:
- Session data: Utilized to retrieve the user's email and validate their status.
- User's cart: A list of cart items for the user, used to calculate total order costs.

Algorithms:
- Cost Calculation: The algorithm to calculate order cost involves multiplying item prices by their respective quantities and summing these up.
- Tax Calculation: Uses a straightforward percentage calculation (9% of the order cost rounded to 2 decimals).
"""

from flask import Blueprint, render_template, session, redirect, flash, request
from .modules.models.user_model import Users
from .modules.models.product_model import Products
import requests
from dotenv import load_dotenv
import os
from .db import db


checkout_blueprint = Blueprint('checkout', __name__)

@checkout_blueprint.route("/checkout", methods=['GET', 'POST']) 
def checkout():
    """
    Function:
    - checkout():
    Input: None directly, but operates based on session data.
    Output: Renders the "checkout.html" template with user data, cart items, order cost, taxes, and total order.
    This function retrieves the current user's information and their cart, calculates the necessary costs and totals,
    and renders the checkout page. If a user is not authenticated, it redirects them to the login page.
    """
    curr_user = Users.get_user_by_email(session.get('user'))
    if curr_user == None:
        return redirect('/login')
    else:
        products = Products.get_prod_list()
        cart = curr_user.get_user_cart()
        print(curr_user.email)
        if cart == []:
            flash("There's no products in your cart to checkout!", 'alert-danger')
            return redirect('/cart')
        else:
            order_cost = round(sum(products[item.product-1].price * item.quantity for item in cart), 2)
            taxes = round(order_cost * 0.09, 2)  # Calculating 9% taxes and rounding to 2 decimals
            shipping_cost = 5.00  # Default shipping cost
            total_order = round(order_cost + taxes, 2)
            
            if request.method == "POST":
                confirmed_order(curr_user, total_order)
                return redirect('/orders')
                
    return render_template("checkout.html", user=curr_user, cart_items=cart, order_cost=order_cost, taxes=taxes, total_order=total_order, products=products)

def confirmed_order(curr_user, price):
    shipping = request.form.get('flexRadioDefault') #get the shipping type selected
    address = request.form.get('inputAddress')
    city = request.form.get('inputCity')
    zip = request.form.get('inputZip')
    
    new_price = price + float(shipping)
            
    if shipping == "5.00": #means USPS Priority Mail
        shipping_type = "USPS"
    else: #means First-Class Mail
        shipping_type = "First"
    
    error = None
    
    if not shipping_type:
        error = 'Shipping type required'
        
    fullAddress = address + " " + city + " " + zip
    
    if error is None:
        order = curr_user.place_order(shipping_type, fullAddress, new_price)
        curr_user.clear_cart()
        send_confirmation_email(curr_user.email, order)
        flash("Order placed successfully", 'alert-success')
            

def send_confirmation_email(email, order):
    
    load_dotenv()
    curr_user = Users.query.filter(Users.id == order.owner_id)
    
    api_key = os.getenv('api_key')
    return requests.post(
		"https://api.mailgun.net/v3/sandbox60fe16e5fa4b4a8fa292ffca0e01f166.mailgun.org/messages",
		auth=("api", api_key),
		data={"from": "Mailgun Sandbox <postmaster@sandbox60fe16e5fa4b4a8fa292ffca0e01f166.mailgun.org>",
			"to": [email],
			"subject": f"PyCraft - Order# {order.order_id} Confirmation",
			"text": f"Hello {email}. \nWe have recieved your order and will be shipping it out shortly. \nThank you!"})