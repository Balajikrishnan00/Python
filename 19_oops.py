"""
# object -Class
class Student:
    '''This Class is about Students'''
print(Student.__doc__)

help(Student)
--------------------------------------------
class supermarket:
    '''This class is about supermarkets'''
#print(supermarket.__doc__)
#help(supermarket)
bread=supermarket()
bread.brand='abc'
print(bread.brand)
---------------------------------"""


class supermarket:
    """shiva organic supermarket"""

    def __init__(self, brand, price, discount=0):
        self.brand = brand
        self.price = price
        self.discount = discount


bread = supermarket('abc', 10, 2)
print(bread.price)
print(bread.discount)
# print(supermarket.__dict__)
shampoo = supermarket('xyz', 5, 1)
biscuit = supermarket('bb', 5, 3)

print(biscuit.__dict__)
