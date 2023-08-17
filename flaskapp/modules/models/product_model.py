""" Class Name: Products

    Date Created: 07/31/2023
    Date Last Updated: 08/12/2023
    Programmer: Ronny Almahdi
    
    Description of class:
    This class is to create product items and store them in the database as well as 
    do some basic functions on getting products, removing, etc.
    
    No important Data Structures
    
    No algorithms used here
    
"""
    
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
        """Searches for a product by its id in a list
            
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
        """Will retrieve all of the products in the database

        Returns:
            Products[]: A list of all the products
        """
        return Products.query.order_by(Products.prod_id.asc()).all()
    
    def add_prod(brand, name, price):
        """Adds a product to the list of 

        Args:
            brand (String): The brand of the product being added
            name (String): The name of the product
            price (Float): The price of the product
        """
        default_img = "https://static.nike.com/a/images/t_default/dd38d4b0-4acd-465b-8eff-7c5d168db71a/air-force-1-mid-07-mens-shoes-S1QClz.png"
        product = Products(brand=brand, name=name, price=price, image=default_img)
        db.session.add(product)
        db.session.commit()
    
    
    def remove_extra(id):
        Products.query.filter(Products.prod_id == id).delete()
        db.session.commit()
        
        