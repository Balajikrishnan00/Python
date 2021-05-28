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
------------------------------
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
-----------------------------------------

class Parent:  # super Class
    i=100   # need of super() keyword ,Class Variable
    def __init__(self):
        self.j=200 # no need of super() keyword  ,Self variable
        print('HI Iam super of Constructor')
        self.Test1()
    def Test1(self): # instance Method
        print('super Test1')
    @staticmethod # staticMethod
    def Test2():
        print('StaticMethod')

    @classmethod # classmethod
    def Test3(cls):
        print('ClassMethod')

class child(Parent):

    def __init__(self):
        print('Child Constructor')
        super(child,self).__init__()
        super().Test1()
        super().Test2()
        super().Test3()

    def m1(self):
        print('-------m1 start--------')
        print(super().i)
        #super(child, self).__init__()
        print(self.i)
        print(self.j)
        self.Test1()
        super(child, self).__init__()
        super().Test1()
        super().Test2()
        super().Test3()
        print('-------m1 end---------')

        @classmethod
        def dis(cls):
            print('child class method')
            #super().Test1()
c1=child()

#c1.Test1()
#print('--------------------------------')
#c1.m1()
#p1=Parent()
#p1.Test2()
#p1.Test3()
#p1.Test1()


# super() -> class variable,instance method,staticmethod,classmethod
# using in child class constructor,child class instance Method
-----------------------------------------------------------------"""
class Patent:
    def __init__(self):
        print('Parent Constructor')
    def InsMethod(self):
        print('ParentInsMethod')
    @staticmethod
    def StaticMethod():
        print('Parent StaticMethod')
    @classmethod
    def ClassMethod(cls):
        print("Parent ClassMethod")

class Child(Patent):
    def __init__(self):
        print('Child Constructor')
    def Method1(self):
        print('Child Ins Method1')
    @staticmethod
    def MethodStatic():
        print('Child StaticMethod')

    @classmethod
    def MethodClass(cls):
        print('Child ClassMethod')
object1=Child()
object1.Method1()
object1.MethodStatic()
object1.MethodClass()
object1.InsMethod()
object1.StaticMethod()
object1.ClassMethod()
object2=Patent()
