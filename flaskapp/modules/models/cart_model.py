from ...db import db
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
        
    def update_quantity(owner, product):
        owner_id = owner.get_id()
        query = Cart.query.filter(Cart.owner_id == owner_id, Cart.brand == product.brand, Cart.name == product.name).first()
        
        query.quantity = query.quantity + 1
        try:
            db.session.commit()
        except:
            print('error updating quantity')
        
    def update_cart_quantity(owner, item, new_quantity):
        owner_id = owner.get_id()
        #gets the item
        user_item = Cart.query.filter(Cart.owner_id == owner_id, Cart.brand == item.brand, Cart.name == item.name).first()
        
        #updates its quantity
        user_item.quantity = new_quantity
        try:
            db.session.commit()
        except:
            print('error updating quantity')
        
        
    def cart_add_item(owner, product):
        #check if the user already has it
        #if they do, just ugpdate the quantity +1
        owner_id = owner.get_id()
        if Cart.already_in_cart(owner_id, product) == True:
            Cart.update_quantity(owner, product)
            print("item quantity changed")
        else:
            added_item = Cart(owner_id = owner_id, brand=product.brand, name=product.name, price=product.price, quantity = 1)
            print(added_item.owner_id)
            print(owner.get_id())
            db.session.add(added_item)
            db.session.commit()
            print("item added")
        
    def remove_item(id_to_remove):
        Cart.query.filter(Cart.cart_id == id_to_remove).delete()
        db.session.commit()
        
    def already_in_cart(owner_id, product):
        query = Cart.query.filter(Cart.owner_id == owner_id, Cart.brand == product.brand, 
                                  Cart.name == product.name).first()
        if query == None:
            return False
        else:
            return True
        
    
        
        
    