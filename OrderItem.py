from Product import Product
from Order import Order

class OrderItem:
    def __init__(self, quantity, unitary_price, order : Order, product : Product):
            self.quantity = quantity 
            self.unitary_price = unitary_price 
            self.order = order
            self.product = product
       