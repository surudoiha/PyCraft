def test_get_name(product):
    assert product.get_name() == "TestProduct"

def test_get_price(product):
    assert product.get_price() == 99.99
