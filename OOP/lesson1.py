class Item:
    # There methods are called magic methods
    # name:str, ensures only string value is passed.
    # what if we want to ignore negative numbers?
    # Let's see it with triggers!

    def __init__(self, name:str, price:float, quantity=0):

        #Run validations to the received parameters
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calcualte_total_price(self):
        return self.price * self.quantity
    
item1 = Item("Phone", 100, 2)
item2 = Item("Laptop", 3000, 4) # Try with minus signs

print(item2.calcualte_total_price())

        