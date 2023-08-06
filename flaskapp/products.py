from flask import Blueprint, render_template, session, redirect, url_for
from flask_login import current_user
from flask import flash



from .db import db, Users, Cart

products_blueprint = Blueprint('products', __name__)

class Products():
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price
    
prods = [Products("Shoe", "Nike", 129.99), Products("Shirt", "Adidas", 199.99), 
         Products("Mrbeast", "YT", 399.99), Products("Mrbeast2", "YT", 399.99)]

@products_blueprint.route("/products/add_to_cart/<int:product_id>", methods=['GET'])
def add_to_cart(product_id):
    curr_user = Users.query.filter(Users.email == session.get('user')).first()
    if curr_user == None:
        return redirect('/login')
    else:
        if product_id is not None and 0 <= product_id < len(prods):
            product = prods[product_id]
            cart_item = Cart(owner_id=curr_user.id, brand=product.brand, name=product.name, price=product.price, quantity=1)
            db.session.add(cart_item)
            db.session.commit()
            flash("Product added successfully", "alert-success") 

    return redirect(url_for('products.products'))

@products_blueprint.route("/products")
def products():
    curr_user = Users.query.filter(Users.email == session.get('user')).first()
    if curr_user == None:
        return redirect('/login')
    else:
        print(curr_user)
        return render_template("products.html", products = prods, user=curr_user)
    
@products_blueprint.route("/cart")
def cart():
    curr_user = Users.query.filter(Users.email == session.get('user')).first()
    if curr_user == None:
        return redirect('/login')
    else:
        cart_items = Cart.query.filter(Cart.owner_id == curr_user.id).all()
        return render_template("cart.html", cart_items=cart_items, user=curr_user)
