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
---------------------------------------"""
