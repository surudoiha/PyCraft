from flaskapp.modules.models.cart_model import Cart
from flaskapp.modules.models.user_model import Users
from flaskapp.modules.models.product_model import Products

def test_add_item(app, user, product):
    curr_user = Users.query.first()
    prod = Products.query.first()
    curr_user.add_item(prod)
    
    with app.app_context():
        assert Cart.query.filter(Cart.owner_id == curr_user.id).first().cart_id == 1
        assert Cart.query.filter(Cart.owner_id == curr_user.id).first().quantity == 1

        
        curr_user.add_item(prod)
        #check to see if it went to the if because prod already in cart
        assert Cart.query.filter(Cart.owner_id == curr_user.id).first().quantity == 2

def test_update_quantity(app, user, product, cart):
    curr_user = Users.query.first()
    prod = Products.query.first()
    Cart.update_quantity_by_1(curr_user, prod)
    
    with app.app_context():
        assert Cart.query.filter(Cart.owner_id == curr_user.id).first().quantity == 2
        
        
def test_update_cart_quantity(app, user, product, cart):
    curr_user = Users.query.first()
    prod = Products.query.first()
    Cart.update_cart_quantity(curr_user, prod, 5)
    
    with app.app_context():
        assert Cart.query.filter(Cart.owner_id == curr_user.id).first().quantity == 5
        
def test_remove_cart_item(app, user, product, cart):
    curr_user = Users.query.first()
    cart_item = Cart.query.filter(Cart.owner_id == curr_user.id).first()
    Cart.remove_item(cart_item.cart_id)
    
    with app.app_context():
        assert Cart.query.filter(Cart.owner_id == curr_user.id).all() == []
        
def test_already_in_cart(app, user, product, cart):
    curr_user = Users.query.first()
    prod = Products.query.first()
    
    result = Cart.already_in_cart(curr_user.id, prod)
    
    with app.app_context():
        assert result == True