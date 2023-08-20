""" Class Name: Order_Model
    
    Date of Creation: 8/13/2023
    Date Updated: 8/17/2023
    
    Description of class:
    This class is to place a users order and save it to the database when they
    are satisfied with the items in their cart.
    
    No important Data Structures
    
    No algorithms used here
"""

from ...db import db
from sqlalchemy.types import JSON
from .product_model import Products
from .cart_model import Cart

class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    order_items = db.Column(JSON)
    shipping_type = db.Column(db.String(50))
    address = db.Column(db.String(100))
    price = db.Column(db.Float)
        
    def get_order_items(self):
        return self.order_items
    
    def place_order(owner_id, shipping_type, address, price):
        """_summary_
            Places an order based on the users current cart.

        Args:
            owner_id (int): The customer who is placing an order
        """
        cart_items = Cart.query.filter_by(owner_id=owner_id).all()
        
        # Build items JSON dict
        items = {}
        for item in cart_items:
            product = Products.query.get(item.product)
            items[product.prod_id] = {
                "name": product.name,
                "brand": product.brand, 
                "price": product.price,
                "quantity": item.quantity  
            }
        
        order = Orders(owner_id=owner_id, order_items=items, shipping_type=shipping_type, address=address, price=price)
        db.session.add(order)
        db.session.commit()
        
        return order
    
    def order_delete(id_to_remove):
        """_summary_
            Removes an order
        Args:
            id_to_remove (int): Order_ID that will be used to delete that order
        """
        Orders.query.filter(Orders.order_id == id_to_remove).delete()
        db.session.commit()
        
#testing how to print the items of order
#    def print_order_items(order_id):
#        order = Orders.query.filter(Orders.order_id == order_id).first()
#        cart_items = order.get_order_items()
#
#        for prod_id, item in cart_items.items():
#            print(f"Product ID: {prod_id}")
#            print(f"Product Name: {item['name']}")
#            print(f"Product Brand: {item['brand']}")
#            print(f"Product Price: {item['price']}")
#            print(f"Quantity: {item['quantity']}")
#            print("---------------")
        
        

        