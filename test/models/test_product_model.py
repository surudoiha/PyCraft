import pytest
from flaskapp.modules.models.product_model import Products

def test_get_name(product):
    assert product.get_name() == "TestProduct"

def test_get_price(product):
    assert product.get_price() == 99.99

def test_get_id(product):
    assert product.get_id() is not None

def test_get_prod_by_id():
    prod_list = [
        Products(brand="Nike", name="Air Max", price=150.0),
        Products(brand="Adidas", name="Superstar", price=80.0),
        Products(brand="Puma", name="Clyde", price=90.0)
    ]
    prod_id = prod_list[1].prod_id  # existing product ID
    assert Products.get_prod_by_id(prod_list, prod_id) == prod_list[0]  #there is one more added in fixtures

    non_existent_prod_id = 999  # A non-existent product ID
    assert Products.get_prod_by_id(prod_list, non_existent_prod_id) is None

def test_add_prod(app):
    with app.app_context():
        Products.add_prod("Adidas", "Superstar", 80.0)
        product = Products.query.first()
        assert product is not None
        assert product.brand == "Adidas"
        assert product.name == "Superstar"
        assert product.price == 80.0

def test_remove_extra(app):
    with app.app_context():
        Products.add_prod("Puma", "Clyde", 90.0)
        product = Products.query.first()
        assert product is not None

        Products.remove_extra(product.prod_id)
        product = Products.query.first()
        assert product is None