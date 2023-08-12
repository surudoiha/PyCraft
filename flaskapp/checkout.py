from flask import Blueprint, render_template, session, redirect
from .modules.models.user_model import Users


checkout_blueprint = Blueprint('checkout', __name__)

@checkout_blueprint.route("/checkout") 
def checkout():
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