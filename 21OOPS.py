"""
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def DoWork(self):
        print('Working')

print(dir(Human))
for x in dir(Human):
    if str(x):

        print(x,'string')
    elif dict(x):
        for i,j in dict(x).items():
            print('dict')
    else:
        print('Other')
------------------------------
#print('hello')

#print(print('hai'),print('Welcome'))
# output
#   hello
#   hai
#   Welcome
#   None None
------------------------------------
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def DoWork(self):
        print('Working')
    def __str__(self):
        return 'Welcome to Human Class'
class Employee(Human):
    def __init__(self,name,age,Empno,EmpSalary):
        super(Employee,self).__init__(name,age)
        self.empno=Empno
        self.empsalary=EmpSalary
    def __str__(self):
        return 'Welcome to EMP Class'

emp1=Employee('balaji',24,101,20000)
print(emp1.empno)
print(emp1.name)
print(emp1)
cus1=Human('siva',25)
print(cus1)
print(cus1.name)
print(cus1.age)
-----------------------------------

class Grandpa:
    def car(self):
        print('Grandpa car')
class Father(Grandpa):
    def bike(self):
        print('Father Bike')
class mother:
    def Scooty(self):
        print('Mother Scooty')

class me(Father,mother):
    def cycle(self):
        print('child cycle')


iam=me()
iam.bike()
iam.car()
iam.Scooty()
iam.cycle()
-----------------------------------

# hierarchical Inheritance

class Honda:
    def getHondasalaty(self):
        print('Honda salary')

class bike(Honda):
    def designBike(self):
        print('Bike designing')

class car(Honda):
    def designCar(self):
        print('Designing Car')

b1=bike()
b1.designBike()
b1.getHondasalaty()

c1=car()
c1.designCar()
c1.getHondasalaty()

h1=Honda()
h1.getHondasalaty()
------------------------------"""
class Maruti:
    def giveSalary(self):
        print('Maruti Give Salary')

class Suzuki:
    def giveSalary(self):
        print('Suzuki Give Salary')

class MarutiSuzuki(Suzuki,Maruti):
    def giveSalary(self):
        print('MarutiSuzuki Give salary')
        Suzuki.giveSalary(self)
        Maruti.giveSalary(self)



ms1=MarutiSuzuki()
ms1.giveSalary()

Maruti.giveSalary(self='Maruti')
Suzuki.giveSalary(self='Suzuki')

Maruti.giveSalary(self=Maruti)
Suzuki.giveSalary(self=Suzuki)