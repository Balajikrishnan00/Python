class customer:
    ''' This class is about bank'''
    bank='Indian Overseas Bank'
    def __init__(self,name,acno,blance):
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