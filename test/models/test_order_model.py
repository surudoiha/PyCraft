import pytest
from flaskapp.modules.models.order_model import Orders
from flaskapp.modules.models.user_model import Users
from flaskapp.modules.models.product_model import Products
from flaskapp.db import db

# For Orders
def test_order_creation(app, user):
    with app.app_context():
        order = Orders.place_order(owner_id=user.id, shipping_type="Standard", address="123 Main St", price=100.0)
        saved_order = db.session.get(Orders, order.order_id)
        assert saved_order is not None

def test_order_deletion(app, user):
    with app.app_context():
        order = Orders.place_order(owner_id=user.id, shipping_type="Standard", address="123 Main St", price=100.0)
        Orders.order_delete(order.order_id)
        deleted_order = db.session.get(Orders, order.order_id)
        assert deleted_order is None


def test_retrieving_orders_for_user(app, user):
    with app.app_context():
        order1 = Orders.place_order(owner_id=user.id, shipping_type="Standard", address="123 Main St", price=100.0)
        order2 = Orders.place_order(owner_id=user.id, shipping_type="Express", address="123 Main St", price=150.0)

        user_orders = Orders.query.filter_by(owner_id=user.id).all()

        assert len(user_orders) == 2
        assert order1 in user_orders
        assert order2 in user_orders

