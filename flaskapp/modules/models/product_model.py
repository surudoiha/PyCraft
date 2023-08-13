product_id = 0
from ...db import db
class Products(db.Model):
    prod_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    brand = db.Column(db.String(50))
    name = db.Column(db.String(50))
    price = db.Column(db.Float)
    image = db.Column(db.String(255))
    
    def __repr__(self):
        return f'<Product ID: {self.prod_id}, Brand+Name+Price: {self.brand} {self.name} {self.price}>'
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_id(self):
        return self.id
    

    def get_prod_by_id(prod_list, prod_id):
        """_summary_
            Searches for a product by its id in a list
            
        Args:
            prod_list (List): the list of the products on the website
            prod_id (int): id of the product you're looking for

        Returns:
            _type_: int
        """
        #for loop that returns index of prod
        for i in range(len(prod_list)):
            if prod_list[i].id == prod_id:
                return prod_list[i]
            else:
                return None
    
    def get_prod_list():
        return Products.query.order_by(Products.prod_id.asc()).all()
    
    def save_to_product_list(product, list):

        list.extend(product)
    
    def add_prod(brand, name, price):
        default_img = "https://static.nike.com/a/images/t_default/dd38d4b0-4acd-465b-8eff-7c5d168db71a/air-force-1-mid-07-mens-shoes-S1QClz.png"
        product = Products(brand=brand, name=name, price=price, image=default_img)
        db.session.add(product)
        db.session.commit()
    
    
    def remove_extra(id):
        Products.query.filter(Products.prod_id == id).delete()
        db.session.commit()

