from flaskapp.modules.models.user_model import Users
from flaskapp.modules.models.product_model import Products
from flaskapp.modules.models.cart_model import Cart
import pytest
from flaskapp import create_app
from flaskapp.db import db

@pytest.fixture(scope="module")
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def product(app):
    with app.app_context():
        default_img = "https://static.nike.com/a/images/t_default/dd38d4b0-4acd-465b-8eff-7c5d168db71a/air-force-1-mid-07-mens-shoes-S1QClz.png"
        product = Products(brand="TestBrand", name="TestProduct", price=99.99, image=default_img)
        db.session.add(product)
        db.session.commit()
        yield product
        db.session.delete(product)
        db.session.commit()

@pytest.fixture(scope='function')
def user(app):
    with app.app_context():
        user = Users(email="test@example.com")
        db.session.add(user)
        db.session.commit()
        yield user
        db.session.delete(user)
        db.session.commit()

def test_root_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to PyCraft!' in response.data

def test_product_page(client, product, user):
    curr_user = Users.query.first()
    client.post('/login', data={"email": curr_user.email})
    products = Products.get_prod_list()
    response = client.get('/products')
    
    assert response.status_code == 200
    assert b"<em>Testing</em>" in response.data
    
    
def test_product_adding(client, user, product):
    curr_user = Users.query.first()
    client.post('/login', data={"email": curr_user.email})
    products = Products.get_prod_list()
    client.get('/products/add_to_cart/1')
    
    user_cart = Cart.query.filter(Cart.owner_id == curr_user.id).first()
    
    assert Products.query.first().prod_id == user_cart.product
    