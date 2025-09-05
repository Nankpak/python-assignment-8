"""
TASK: Create a ShoppingCart class.

Requirements:
1. Store cart items in a dictionary (item → quantity).
2. Provide a method to add items.
3. Provide a method to remove items.
4. Provide a method to clear the cart.
5. Provide a method to calculate total price (with price list).

Example Usage:
    prices = {"Shirt": 5000, "Shoes": 12000}
    cart = ShoppingCart(prices)
    cart.add_item("Shirt", 2)
    print(cart.calculate_total())  # 10000
    cart.remove_item("Shirt", 1)
    print(cart.calculate_total())  # 5000
"""
class ShoppingCart:
    def __init__(self,price):
        self.price = {'shirt':5000,'shoes':12000}
    def add_item(self,add):
        return self.price.update({'add':5000*2})
    def remove_item(self,shirt):
        return self.price.update({'shirt':5000*1})

cart1 =ShoppingCart('prices')
print(cart1.price)
print(cart1.add_item(2))
print(cart1.remove_item(1))