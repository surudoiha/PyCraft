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
from flask import Blueprint, render_template, session, redirect
from .modules.models.user_model import Users

checkout_blueprint = Blueprint('checkout', __name__)

@checkout_blueprint.route("/checkout") 
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
        cart = curr_user.get_user_cart()
        order_cost = round(sum(item.price * item.quantity for item in cart), 2)
        taxes = round(order_cost * 0.09, 2)  # Calculating 9% taxes and rounding to 2 decimals
        shipping_cost = 5.00  # Default shipping cost
        total_order = round(order_cost + taxes + shipping_cost, 2)
        print("Order Cost:", order_cost)
        print("Taxes:", taxes)
        print("Total Order:", total_order)

    return render_template("checkout.html", user=curr_user, cart_items=cart, order_cost=order_cost, taxes=taxes, total_order=total_order)