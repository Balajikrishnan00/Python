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
------------------------------------"""
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
