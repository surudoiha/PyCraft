from flaskapp.modules.models.user_model import Users
from flaskapp.modules.models.product_model import Products
from flaskapp.modules.models.cart_model import Cart

def test_get_user_by_email(app, user):
    queried_user = Users.get_user_by_email("test@example.com")
    assert queried_user == user

def test_in_database(app, user):
    assert user.in_database() == True
    new_user = Users(email="new@example.com")
    assert new_user.in_database() == False

def test_get_id(app, user):
    assert user.get_id() == user.id

def test_get_user_cart(app, user, product):
    user.add_item(product)
    user_cart = user.get_user_cart()
    assert len(user_cart) == 1
    assert user_cart[0] is not None

def test_clear_cart(app, user):
    user.clear_cart()
    assert len(user.get_user_cart()) == 0

def test_place_order(app, user):
    shipping_type = "Standard"
    address = "123 Main St"
    price = 100.0

    order = user.place_order(shipping_type, address, price)
    assert order is not None
    assert order.shipping_type == shipping_type
    assert order.address == address
    assert order.price == price

def test_add_item(app, user, product):
    user.add_item(product)
    user_cart = user.get_user_cart()
    assert len(user_cart) == 1
    assert user_cart[0] is not None
    
# Add more 
    """
        test_in_database_returns_true_for_existing_user
        test_in_database_returns_false_for_nonexistent_user
        test_register_user
        test_authenticate
        test_add_item_to_user_cart
        test_get_user_cart
    """