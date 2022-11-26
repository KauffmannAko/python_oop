class Item:

    #class attribute
    pay_rate = 0.8
    objs = []

    """__init__ constructor
    """
    #
    def __init__(self, name: str, price:int, quantity: int):

        #Data validation
        assert type(name) == str, "{} must be a string".format(name)
        #assert type(price) == int and price >= 0, "{} must be an int or positive".format(price)
        #assert type(quantity) == int, "{} must be an int".format(quantity)

        #Assign self to object
        self.name = name
        self.price = price
        self.quantity = quantity

        # add every instance of the class to objs list
        Item.objs.append(self)


    def calcTotalPrice(self):
        return self.price * self.quantity
    def apply_discount(self):
        #take note of Item.pay_rate
        #self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate
    
    def __repr__(self):
        """
        our list of objs. is like so 
        [<__main__.Item object at 0x7f0ea0fbab20>, <__main__.Item object at 0x7f0ea0f502e0>, <__main__.Item object at 0x7f0ea0f1a670>,
         <__main__.Item object at 0x7f0ea0f1ad30>, <__main__.Item object at 0x7f0ea0f1ad90>]

         and we want it do be more friendlt

        """
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"
        pass


#print(Item.pay_rate)

#item1 = Item("nana",3300, 20)
#print(Item.__dict__) # Give all attributes at class level
#print(item1.__dict__) #Give all attributes at instance level
#item1.pay_rate = 0.7
#print(item1.apply_discount())
#print(item1.__dict__)
#print(item1.name)


#five instances 
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
print(Item.objs)

for instance in Item.objs:
    print(instance.price)

