from flask import Blueprint, render_template, session
from .modules.models.user_model import Users


checkout_blueprint = Blueprint('checkout', __name__)

@checkout_blueprint.route("/checkout") 
def checkout():
    email = session.get('user_email')
    user = None

    if email:
        user = Users.get_user_by_email(email)
        cart = user.get_user_cart()  

        order_cost = sum(item['price'] * item['quantity'] for item in cart)
        taxes = round(order_cost * 0.09, 2)  # Calculating 9% taxes and rounding to 2 decimals
        total_order = order_cost + taxes  # Adding the taxes to the order cost

        return render_template("checkout.html", user=user, order_cost=order_cost, taxes=taxes, total_order=total_order)

    return render_template("checkout.html", user=None)



