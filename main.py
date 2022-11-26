class Item:


    """__init__ constructor
    """
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






item1 = Item("Bicycle",-400,4)
print(item1.calcTotalPrice())
