"""
import sys
class customer:
    ''' This class is about bank'''
    bank='Indian Overseas Bank'
    def __init__(self,name,acno,blance=500):
        self.name=name
        self.acno=acno
        self.blance=blance
        print('welcome Mr.',self.name,'How can help you')

    def deposit(self,amt):
        self.blance+=amt

    def withdraw(self,amt):
        if self.blance>=500 and self.blance-amt>=500 :
            self.blance -= amt
        else:
            print('sorry you have only minimum balance only')

print('Welcome to',customer.bank)
name=input('whats is your name:')
acno=int(input('Ac number:'))
c1=customer(name,acno,500)
c1.deposit(500)
print(c1.blance)
c1.withdraw(200)
print(c1.blance)
c1.withdraw(300)
print(c1.blance)
c1.withdraw(100)
#print(c1.blance)
----------------------------------
import sys
class bank:
    bankName='Indian Overseas Bank'
    '''this class is about bank'''
    def __init__(self,name,accno,blance=500):
        self.name=name
        self.accno=accno
        self.blance=blance
        print('Welcome to ',bank.bankName,'Mr.',self.name)


    def deposit(self,amount):
        self.blance+=amount
    def blanceEnquiry(self):
        print('Your amount:',self.blance)
    def widthraw(self,amount):
        if self.blance>=500 and self.blance-amount>=500:
            self.blance-=amount
        else:
            print('sorry minimum balance must be maintain is 500.00')
    def exit(self):
        sys.exit()


name=input('acHolder Name:')
accno=int(input('ac Number:'))
c=bank(name, accno)

while True:

    choice =input('D-Deposit\nB-Balance Enquiry\nW-Widthraw\nS-Exit\n')

    if choice=='D' or choice=='d':
        #c=bank(name, accno)
        amt=float(input('Enter your amount:'))
        c.deposit(amt)

    elif choice=='B' or choice=='b':
        c.blanceEnquiry()

    elif choice=='W' or choice=='w':
        amt=float(input('Enter Widthraw amount:'))
        c.widthraw(amt)


    elif choice=='S' or choice=='s':
        sys.exit()
---------------------------------------
# inheritance
# 1. HAS A relationship
# 2. IS A relationship

class Engine:
    '''This class is about Engine'''
    mileage=22

    def __init__(self):
        self.petrol=True
        self.Engine_Running=False
    def EngineStart(self):
        if self.Engine_Running:

            print('Engine Already Running')
        else:
            self.Engine_Running=True
            print('Engine Started...')

    def EngineStop(self):
        if self.Engine_Running:
            self.Engine_Running=False
            print('Engine Stopped..!')
        else:
            print('Engine Already Stopped..!')
class Car:
    '''This class is about Car'''
    def __init__ (self):
        self.engine=Engine()
    def drive(self):
        self.engine.EngineStart()
        print('Car in Running')

    def park(self):
        self.engine.EngineStop()
        print('Car stoped')
c1=Car()
c1.drive()
c1.park()
#t1=Engine()
#t1.EngineStart()
#t1.EngineStart()
#t1.EngineStop()
#t1.EngineStop()
------------------------------
# 2 is a relationship

class humanbeing:
    '''this class about is humanbeing'''
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def reading(self):
        print('reading books')
class empolyee(humanbeing):
    '''this class is about employee'''
    def __init__(self,empno,salary,name,age,sex):
        super().__init__(name,age,sex)
        self.empno=empno
        self.salary=salary
    def dowork(self):
        print('Emp working')
emp1=empolyee(101,20000,'balaji',24,'male')

print(emp1.age)
emp1.reading()
emp1.dowork()
-----------------------------------------------
class bank:
    bankname='SBI'
    def __init__(self):
        self.min=2000
    def deposit(self):
        print('Deposit')
    def withdraw(self):
        print('widthraw')
    @staticmethod
    def staticmethod():
        print('staticmethod is running')
    @classmethod
    def classmethod(cls):
        print('classmethod is running',cls.bankname)

user1=bank()
user1.classmethod()
user1.staticmethod()
user1.deposit()
user1.withdraw()
print(user1.min)
----------------------------------
class Signup:
    '''This class is about  Signup your account'''
    def __init__(self,name,accno):
        self.name=name
        self.accno=accno
        self.account=True
class Rbi(Signup):
    '''This class is about Bank'''
    def __init__(self,acname,acno):
        super(Rbi,self).__init__(acname,acno)
    def deposit(self):
        if self.account:
            print('cash Deposited')
        else:
            print('Please Login')
    def withdraw(self):
        if self.account:
            print('cash withdraw success full.')
        else:
            print('Login')
class indianBank(Rbi):
    @staticmethod
    def staticmethod():
        print('staticmethod is running')

#user1=indianBank('balaji',12234)
#user1.deposit()
#user1.withdraw()
#print(user1.account)
#user1.staticmethod()
user2 =indianBank()
user2.deposit()
---------------------------------------
# multiple inheritance

class RBI:
    def Loan(self):
        print('Loan')
    def loadthallupadi(self):
        print('Getting done')

class SBI(RBI):
    def deposite(self):
        print('Deposited')
    def withdraw(self):
        print('Withdraw')
class LBank(SBI):
    pass
l1=LBank()
l1.Loan()
l1.deposite()

----------------------------
class Bank1:
    def deposite(self):
        print('Deposite amount')
    def withdraw(self):
        print('Withdraw')
class Bank2:
    def AgriLoad(self):
        print('Got AgriLoan')
    def EducationLoan(self):
        print('You Got Education Loan')
class Bank3(Bank2,Bank1):
    pass
user1=Bank3()
user1.deposite()
user1.withdraw()
user1.AgriLoad()
user1.EducationLoan()
------------------------------
class lali:
    address='chennai'
    def __init__(self):
        self.Ho_OFFER=1000
    def MegaOffer(self):
        print('Mega Offer')
class lali1(lali):
    def __init__(self):
        super(lali1,self).__init__()
        self.L_OFFE=500
    def LocalOffer(self):
        print('Local 0ffer')

c1=lali1()
#c1.Ho_OFFER
print(c1.address)
print(c1.L_OFFE)
print(c1.Ho_OFFER)
c1.MegaOffer()
c1.LocalOffer()

-----------------------------
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class employee(Human):
    '''This class is about Employee'''
    def __init__(self,name,age,empno,salary):
        super(employee,self).__init__(name,age)

        self.emp=empno
        self.salary=salary
#emp1=employee('balaji',24,101,2000)
emp2=employee('siva',24,102,40000)

print(emp2.__doc__)
print(emp2.__dict__)
-----------------------------
# Multilevel Bank
class HeadBank:
    def EDULoan(self):
        print('Edu Loan')
    def AgriLoan(self):
        print('AgriLoan')


class SBI(HeadBank):
    def Saving(self):
        print('Savings')
    def Deposit(self):
        print('Deposit')
    def Widthraw(self):
        print('withdraw')

class OppBank(HeadBank):
    pass



class VillageBank(SBI):
    def NEWaccount(self):
        print('New User')

c1=VillageBank()
c1.EDULoan()
c1.Saving()
c1.NEWaccount()
---------------------------"""
