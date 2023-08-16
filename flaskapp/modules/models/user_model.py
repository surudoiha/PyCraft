""" Class Name: Users

    Date Created: 07/23/2023
    Date Last Updated: 08/01/2023
    Programmer: Ronny Almahdi
    
    Description of class:
    This class is for the main User creation and functions needed for a
    customer to be able to do most of their shopping and ordering.
    
    No important Data Structures
    
    No algorithms used here
"""


from ...db import db
from flask_login import current_user, UserMixin
from .cart_model import Cart

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    email = db.Column(db.String(50), nullable = False, unique = True)
        
    def __repr__(self):
            return f'<User: {self.id}, Email:{self.email}>'
        
    
    def get_user_by_email(email):
        """Gets the user by their email
        
        Args:
            email (string): email of user you're getting from db

        Returns:
            Users: returns the user obj in the db
        """
        user = Users.query.filter(Users.email == email).first()
        return user
    
    def in_database(self):
        """Checks to see if the user is in the database

        Returns:
            boolean: True if in db, False if not in db
        """
        user = Users.query.filter(Users.email == self.email).first()
        if user == None:
            return False
        else:
            return True
        
    def register_user(self):
        #query DB and add the user
        print()
        
    def authenticate(self):
        print()
        
    def add_item(self, product):
        """Adds an item to the user's cart.
            
        Args:
            product (Product): The product we are adding
        """
        #deligation
        Cart.cart_add_item(self, product)
        
    def get_user_cart(self):
        """Gets the users cart and all the items in it
        
        Returns:
            Cart[]: The cart list of all the cart objs in it
        """
        user = Users.query.filter(Users.email == self.email).first()
        user_cart = Cart.query.filter(Cart.owner_id == user.id).all()
        return user_cart
    
    def get_email(self):
        return self.email
    
    def get_id(self):
        user = Users.query.filter(Users.email == self.email).first()
        return user.id