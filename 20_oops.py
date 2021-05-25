class customer:
    ''' This class is about bank'''
    bank='Indian Overseas Bank'
    def __init__(self,name,acno):
        self.name=name
        self.acno=acno
        print('welcome Mr.',self.name,'How can help you')

    def deposit(self,amt):
        pass
    def withdraw(self,amt):
        pass


print('Welcome to',customer.bank)
name=input('whats is your name:')
acno=int(input('Ac number:'))
c1=customer(name,acno)
