class ShoppingCart:
    def __init__(self,customer_id):
        self.customer_id = customer_id
        self.items_present_in_cart = {}
    
    def add_item(self,product,price):
        if product not in self.items_present_in_cart:
            self.items_present_in_cart[product] = price
            print("%s Added" %(product))
        else:
            print("%s already present" %(product))
    
    def remove_item(self,product):
        if product not in self.items_present_in_cart:
            print("%s Not present" %(product))
        else:
            del self.items_present_in_cart[product]
            print("%s removed" %(product))

    
customer = ShoppingCart(1)
customer.add_item("Maggi", 24)
print(customer.__dict__)
customer.add_item("Noodles", 24)
print(customer.__dict__)
customer.remove_item("Maggi")
print(customer.__dict__)
