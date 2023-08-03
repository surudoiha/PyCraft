from ..db import db
class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    brand = db.Column(db.String(50))
    name = db.Column(db.String(50))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    
    def __repr__(self):
        return f'<Cart Owner: {self.owner_id}, Brand+Name+Price: {self.brand} {self.name} {self.price}>'
    
    def get_cart_items(self):
        print('')
        
    def add_product():
        print('')
        
    def remove_product():
        print()
    
    