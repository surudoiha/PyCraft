from ..db import db
from flask_login import current_user, UserMixin
from .cart_model import Cart

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    email = db.Column(db.String(50), nullable = False, unique = True)
        
    def __repr__(self):
            return f'<User: {self.id}, Email:{self.email}>'
        
    def get_user_by_email(email):
        user = Users.query.filter(Users.email == email).first()
        return user
    
    def in_database(self):
        user = Users.query.filter(Users.email == self.email).first()
        if user == None:
            return False
        else:
            return True
        
    def register_user(self):
        #query DB anda add the user
        print()
        
    def authenticate(self):
        print()
        
    def get_user_cart(self):
        user = Users.query.filter(Users.email == self.email).first()
        user_cart = Cart.query.filter(Cart.owner_id == user.id).all()
        return user_cart
    
    def get_email(self):
        return self.email
    
    def get_id(self):
        user = Users.query.filter(Users.email == self.email).first()
        return user.id