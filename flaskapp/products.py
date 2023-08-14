from flask import Blueprint, render_template, session, redirect, url_for, request
from flask_login import current_user
from flask import flash


from .db import db
from .modules.models.user_model import Users
from .modules.models.product_model import Products
from .modules.models.cart_model import Cart

products_blueprint = Blueprint('products', __name__)
prods = Products.get_prod_list()

#Adds Product to DB
@products_blueprint.route("/products/add_to_cart/<int:product_id>", methods=['GET','POST'])
def add_to_cart(product_id):
    curr_user = Users.get_user_by_email(session.get('user'))
    if curr_user == None:
        return redirect('/login')
    else:
        print('ran for {x}'.format(x=product_id) )
        if 1 <= product_id <= len(prods)+1:
            print("inside add_to_cart if ")
            selected_prod = prods[product_id-1]
            if selected_prod != None:
                curr_user.add_item(selected_prod)
                flash("Product added successfully", "alert-success")
        # if product_id is not None and 0 <= product_id < len(prods):
        #     product = prods[product_id]
        #     cart_item = Cart(owner_id=curr_user.id, brand=product.brand, name=product.name, price=product.price, quantity=1)
        #     db.session.add(cart_item)
        #     db.session.commit()
        #     flash("Product added successfully", "alert-success") 

    return redirect(url_for('products.products'))

@products_blueprint.route("/products")
def products():
    curr_user = Users.get_user_by_email(session.get('user'))
    if curr_user == None:
        return redirect('/login')
    else:
        for prod in prods:
            print(prod)
        return render_template("products.html", products = prods, user=curr_user)
    

