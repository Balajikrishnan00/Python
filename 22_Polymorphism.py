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
-------------------------------------"""
class mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def __gt__(self, other):
        return self.price>other.price
m1=mobile('samsung',10000)
m2=mobile('Vivo',12000)

print(m1>m2)

