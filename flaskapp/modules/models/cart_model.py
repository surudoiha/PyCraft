""" Class Name: Products

    Date Created: 08/03/2023
    Date Last Updated: 08/10/2023
    Programmer: Ronny Almahdi
    
    Description of class:
    This class is to add items to a users cart and to do updating, searching,
    deleting, and adding items to the users cart.
    
    No important Data Structures
    
    No algorithms used here
    
"""

from ...db import db
class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product = db.Column(db.Integer, db.ForeignKey('products.prod_id'))
    quantity = db.Column(db.Integer)
    
    def __repr__(self):
        return f'<Cart Owner: {self.owner_id}, Cart ID: {self.cart_id}>, Quantity: {self.quantity}'
    
    def get_cart_items(self):
        print('')
        
    def update_quantity_by_1(owner, item):
        """Will update the quantity of an item in the users cart by 1.
            
        Args:
            owner (Users): User that we are updating the product's quantity in their cart
            item (Product): The product we are updating the quantity for
        """
        owner_id = owner.get_id()
        query = Cart.query.filter(Cart.owner_id == owner_id, Cart.product == item.prod_id).first()
        
        query.quantity = query.quantity + 1
        try:
            db.session.commit()
        except:
            print('error updating quantity')
        
    def update_cart_quantity(owner, item, new_quantity):
        """Updating cart's quanity to a new quantity
            
        Args:
            owner (Users): User that we are updating the product's quantity in their cart
            item (Product): The product we are updating the quantity for
            new_quantity (int): The new quantity we will set the product in the cart to
        """
        owner_id = owner.get_id()
        #gets the item
        user_item = Cart.query.filter(Cart.owner_id == owner_id, Cart.product == item.product).first()
        
        #updates its quantity
        user_item.quantity = new_quantity
        try:
            db.session.commit()
        except:
            print('error updating quantity')
        
        
    def cart_add_item(owner, item):
        """Creating a cart obj to hold the item the user wants to add to their cart
        
        Args:
            owner (Users): User that we are adding the product to their cart
            product (Product): The product we are adding to cart
        """
        
        #check if the user already has it
        #if they do, just ugpdate the quantity +1
        owner_id = owner.get_id()
        if Cart.already_in_cart(owner_id, item) == True:
            Cart.update_quantity_by_1(owner, item)
            print("item quantity changed")
        else:
            added_item = Cart(owner_id = owner_id, product=item.prod_id, quantity = 1)
            db.session.add(added_item)
            db.session.commit()
            print("item added")
        
    def remove_item(id_to_remove):
        """Removes an item from the user's cart
        
        Args:
            id_to_remove (int): The cart's id of the item to remove
        """
        Cart.query.filter(Cart.cart_id == id_to_remove).delete()
        db.session.commit()
        
    def already_in_cart(owner_id, product):
        """Checks to see if the product is already in the users cart
            
        Args:
            owner_id (int): The id of the user's cart we are checking
            product (Product): The product we are looking to see if in the cart

        Returns:
            boolean: True if in cart, False if not in cart
        """
        query = Cart.query.filter(Cart.owner_id == owner_id, Cart.product == product.prod_id).first()
        if query == None:
            return False
        else:
            return True
        
    
        
        
    