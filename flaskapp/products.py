from flask import Blueprint, render_template
from flask_login import current_user

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
    return render_template("products.html", products = prods, user=current_user)