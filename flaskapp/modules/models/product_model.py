class Products():
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def save_to_product_list(product, list):
        
        list.extend(product)
