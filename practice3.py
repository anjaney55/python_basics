'''
Create a class called Order which stores a item & price.
    use the Dunder function __gt__ to convey that 
    order1 > order2 if the price of order1 > price of order2 
'''

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,ord2): #Dunder function '__gt__'
        return self.price > ord2.price # it is used to compare the price of two orders
    
ord1 = Order("Oil",120)
ord2 = Order("Salt",60) 
print(ord1 > ord2) 