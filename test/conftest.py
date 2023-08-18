import pytest
from flaskapp.db import db
from flaskapp.modules.models.product_model import Products
from flaskapp.modules.models.user_model import Users

from flask import Flask  # need Flask to create a mock app

@pytest.fixture()
def app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture(scope='module')
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

@pytest.fixture(scope='module')
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def user(app):
    with app.app_context():
        user = Users(email="test@example.com")
        db.session.add(user)
        db.session.commit()
        yield user
        db.session.delete(user)
        db.session.commit()