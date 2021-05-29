"""
class Bike:
    def Fill(self):
        print('Fill petrol')
class Lorry:
    def Fill(self):
        print('Fill Diesel')
class Ecar:
    def Fill(self):
        print('Fill Power')

class vehiles:
    def Fill(self):
        print('Get Ready for ride')

def charge(a):
    a.Fill()

b=Bike()
l=Lorry()
c=Ecar()
listofvehiles=[b,l,c]

for x in listofvehiles:
    charge(x)
--------------------------------
# operator Overloading
need to deep learn
class book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
        return self.pages+other.pages
    def __mul__(self, other):
        return self.pages*other.pages
    def __mod__(self, other):
        return self.pages % other.pages

b1=book(100)
b2=book(100)
print(b1+b2)
print(b1*b2)
print(b1%b2)
-------------------------------------
class mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def __gt__(self, other):
        return self.price>other.price
m1=mobile('samsung',10000)
m2=mobile('Vivo',12000)

print(m1>m2)
------------------------------
class Mobile:
    def __init__(self,brand,price,offer):
        self.brand=brand
        self.price=price
        self.offer=offer
    def __gt__(self, other):
        return self.price>other.price

    def __add__(self,other):
        return self.offer+other.ccoffer

class CreditCard:
    def __init__(self,ccoffer):
        self.ccoffer=ccoffer
m1=Mobile('samsung',12000,850)
m2=Mobile('vivo',11000,450)
cc=CreditCard(1000)
print(m2>m1)
print(m1+cc)
---------------------------
class Test:
    def calulate(self,*n):
        print('aa')
        total=0
        for i in n:
            total+=i
        print(total)
    #def calulate(self,no1,no2,no3):
    #    print('bbb')

t=Test()
t.calulate(1,2)
#t.calulate(1,2,3)
-------------------------
# constructor overloading

class supermarket:
    def __init__(self,*content):
        print('Constructor')
ob1=supermarket('soap',20,3)
ob2=supermarket('Rice',40)
--------------------------
# Method Overriding
# same method name in Parent and Child
class P:
    def study(self):
        print('Parent study')
class C(P):
    def play(self):
        print('Child Play')
    def study(self):
        super().study()
        print('Child Study')
c=C()
c.study()
P.study(c)

------------------------
# constructor overriding
class Parent:
    def __init__(self):
        print('I am Parent Class Constructor')
    def Method(self):
        print('Parent method')
class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()
        print('Iam Child Constructor')
c=Child()
c.Method()
Parent.__init__(c)
------------------------------"""

# Abstraction
# showing only the Necessary data and Hiding Unwanted
from abc import *
class Indian(ABC):

    @abstractmethod
    def havingBreakfast(self):
        pass

class Tamil(Indian):

    #def havingBreakfast(self):
    pass

        #print('Tamilnadu Breakfast')
    #    print('tamil nadu')
    #def hello(self):
    #    print('Hello')
class chennai(Tamil):
    #pass
    def havingBreakfast(self):
        print('rice dosa')


#t=Tamil()
#t.havingBreakfast()
c=chennai()
c.havingBreakfast()
#c.havingBreakfast()
#Tamil.havingBreakfast(c)
#t.hello()

