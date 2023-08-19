import pytest
from flaskapp.modules.models.order_model import Orders
from flaskapp.modules.models.user_model import Users
from flaskapp.modules.models.product_model import Products
from flaskapp.db import db

# For Orders
def test_order_creation(app, user):
    with app.app_context():
        order = Orders(owner_id=user.id)
        db.session.add(order)
        db.session.commit()
        saved_order = db.session.get(Orders, order.order_id)
        assert saved_order is not None

def test_order_deletion(app, user):
    with app.app_context():
        order = Orders(owner_id=user.id)
        db.session.add(order)
        db.session.commit()
        db.session.delete(order)
        db.session.commit()
        deleted_order = db.session.get(Orders, order.order_id)
        assert deleted_order is None

def test_order_update(app, user):
    with app.app_context():
        order = Orders(owner_id=user.id)
        db.session.add(order)
        db.session.commit()

        order.status = "Shipped"  
        db.session.commit()

        updated_order = db.session.get(Orders, order.order_id)
        assert updated_order.status == "Shipped"

def test_retrieving_orders_for_user(app, user):
    with app.app_context():
        order1 = Orders(owner_id=user.id)
        order2 = Orders(owner_id=user.id)
        db.session.add(order1)
        db.session.add(order2)
        db.session.commit()

        user_orders = Orders.query.filter_by(owner_id=user.id).all()

        assert len(user_orders) == 2
        assert order1 in user_orders
        assert order2 in user_orders
