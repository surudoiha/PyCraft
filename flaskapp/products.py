from flask import Blueprint, render_template, session, redirect
from flask_login import current_user

from .db import db, Users, Cart

products_blueprint = Blueprint('products', __name__)

class Products():
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price
    
prods = [Products("Shoe", "Nike", 129.99), Products("Shirt", "Adidas", 199.99), 
         Products("Mrbeast", "YT", 399.99), Products("Mrbeast2", "YT", 399.99)]

@products_blueprint.route("/products")
def products():
    curr_user = Users.query.filter(Users.email == session['user']).first()
    if curr_user == None:
        return redirect('/login')
    print(curr_user)
    return render_template("products.html", products = prods, user=curr_user)