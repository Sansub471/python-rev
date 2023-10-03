class Item:

    # Class attribute
    # Shared by all instances, it belongs to the class itself
    # it can also be accessed by instances
    pay_rate  = 0.8

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
    

    def apply_discount(self):
        # self.price = self.price * Item.pay_rate
        # The best practice here is to access attributes at class level
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 2)
item2 = Item("Laptop", 3000, 4) # Try with minus signs

print(item2.calcualte_total_price())
print(Item.pay_rate) # accessing at the class level
print(item1.pay_rate) # accessing at the instance level
print(item2.pay_rate) # first check at instance level and then in class level

# All attributes of an object
print(Item.__dict__) # All the attributes of class level
print('\n')
print(item1.__dict__) # All the attributes of the instance level


item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)


        