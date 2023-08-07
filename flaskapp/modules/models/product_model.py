product_id = 0
class Products():
    def __init__(self, name, brand, price):
        global product_id
        product_id = product_id + 1
        self.id = product_id
        self.name = name
        self.brand = brand
        self.price = price
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_id(self):
        return self.id
    
    def get_prod_by_id(prod_list, prod_id):
        for i in range(len(prod_list)):
            if prod_list[i].id == prod_id:
                return prod_list[i]
            else:
                return None
    
    def save_to_product_list(product, list):
        
        list.extend(product)
