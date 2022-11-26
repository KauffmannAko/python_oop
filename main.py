class Item:

    #class attribute
    pay_rate = 0.8

    """__init__ constructor
    """
    #
    def __init__(self, name: str, price:int, quantity: int):

        #Data validation
        assert type(name) == str, "{} must be a string".format(name)
        assert type(price) == int and price >= 0, "{} must be an int or positive".format(price)
        assert type(quantity) == int, "{} must be an int".format(quantity)

        #Assign self to object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calcTotalPrice(self):
        return self.price * self.quantity


#print(Item.pay_rate)

item1 = Item("nana",3300, 20)
#print(Item.__dict__) # Give all attributes at class level
print(item1.__dict__) #Give all attributes at instance level
