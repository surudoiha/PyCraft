product_id = 0
class Products():
    def __init__(self, name, brand, price):
        global product_id
        product_id = product_id + 1
        self.id = product_id
        self.name = name
        self.brand = brand
        self.price = price
        self.image = "https://static.nike.com/a/images/t_default/dd38d4b0-4acd-465b-8eff-7c5d168db71a/air-force-1-mid-07-mens-shoes-S1QClz.png"
    
    
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
    
    def save_to_product_list(product, list):

        list.extend(product)
