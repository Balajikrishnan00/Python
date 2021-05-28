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
