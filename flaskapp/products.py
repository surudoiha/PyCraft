from flask import Blueprint, render_template, session, redirect, url_for, request
from flask_login import current_user
from flask import flash


from .db import db
from .modules.models.user_model import Users
from .modules.models.product_model import Products
from .modules.models.cart_model import Cart

products_blueprint = Blueprint('products', __name__)
    
prods = [Products("Shoe", "Nike", 129.99), Products("Shirt", "Adidas", 199.99), 
         Products("Mrbeast", "YT", 399.99), Products("Mrbeast2", "YT", 399.99)]

#Adds Product to DB
@products_blueprint.route("/products/add_to_cart/<int:product_id>", methods=['GET','POST'])
def add_to_cart(product_id):
    curr_user = Users.get_user_by_email(session.get('user'))
    if curr_user == None:
        return redirect('/login')
    else:
        print('ran for {x}'.format(x=product_id) )
        if 1 <= product_id <= len(prods)+1:
            print("inside add_to_cart if")
            selected_prod = prods[product_id-1]
            print(selected_prod)
            curr_user.add_item(selected_prod)
            flash("Product added successfully", "alert-success")

    return redirect(url_for('products.products'))

@products_blueprint.route("/products")
def products():
    curr_user = Users.get_user_by_email(session.get('user'))
    if curr_user == None:
        return redirect('/login')
    else:
        print("0:{a} 1:{b} 2:{c} 3:{d}".format(a=prods[0].id, b=prods[1].id, c=prods[2].id, d=prods[3].id))
        if request.method == 'POST':
            if request.form['1']:
                print('btn 1 pressed')
            elif request.form['2']:
                print('btn 2 pressed')
            elif request.form['3']:
                print('btn 3 pressed')
            elif request.form['4']:
                print('btn 4 pressed')
        print(curr_user)
        print(prods[1].id)
        return render_template("products.html", products = prods, user=curr_user)
    

