"""
try:
    no1 = int(input('Enter No1:'))
    no2 = int(input('Enter No2:'))
    print(no1 / no2)
except ZeroDivisionError:
    print('Zero division Error')
finally:
    print('Welcome to Balaji')

print(-0*-1)

def sum(a):
    print('balaji')

sum(1)
# Every Exception in Python is a Class
# all Exception classes are child
----------------------------------------
try:
    n1=int(input('Enter Number N1:'))
    n2=int(input('Enter Number N2:'))

    n3=n1/n2
    print(n3)
except ZeroDivisionError:
    print('ZeroDivisionError')
except ValueError:
    print('ValueError')
print('hi')
---------------------------------------
def division(n1,n2):
    try:
        print(n1/n2)
    except ZeroDivisionError:
        print('ZeroDivisionError')
        n1=int(input('Enter n1 number:'))
        n2=int(input('Enter n2 number:'))
        division(n1,n2)
    except ValueError:
        print('ValueError')
        n1=int(input('Enter n1 number:'))
        n2=int(input('Enter n2 number:'))
        division(n1,n2)
    except TypeError:
        print('TypeError')
        n1=int(input('Enter n1 number:'))
        n2=int(input('Enter n2 number:'))
        division(n1,n2)
division(10,'Hello')
---------------------------------------------
def division():
    try:
        n1=int(input('Enter n1 number:'))
        n2=int(input('Enter n2 number:'))
        print(n1/n2)
    except ZeroDivisionError:
        print('ZeroDivisionError')
        
        division()
    except ValueError:
        print('ValueError')
        
        division()
    except TypeError:
        print('TypeError')
    finally:
        print('finally')

        
division()
--------------------------------------------
try:
    print(10+'hello')
except (ZeroDivisionError,ValueError,TypeError):
    print('Something Went Wrong')
-------------------------------------------
# finally

try:
    print('Hi')
except SyntaxError:
    print('Welcome')
finally:
    print('good')


# os.exit() will not use finally
------------------------------------------
try:
    n1=int(input('Enter n1:'))
    n2=int(input('Enter n2:'))
    print('Try1')

    try:
        print(n1/n2)
        print('Try2')
    except(ZeroDivisionError):
        print('ZeroDivisionError')
    finally:
        print('Program Terminated1')
except ValueError:
    print('ValueError')
else:
    print('Else Running') # else part is running without Exception Occured
finally:
    print('Program Terminated2')
----------------------------------------------
class InsufficientBalanceException(Exception):
    def __init__(self,mgs):
        self.mgs=mgs
        #print('Check Your Balance')

class Bank():
    def __init__(self,username,password,blance=0):
        self.username=username
        self.password=password
        self.blance=blance
    def BlanceEnqury(self):
        print('Current Blance is:',self.blance)
    def withdraw(self,amount):

        
        try:
            if self.blance>=500 and self.blance-amount>=500:
                self.blance-=amount

            #print('Current Blance is:',self.blance)
                ibe=InsufficientBalanceException('Check Your Balance')
        
                raise ibe 
        except InsufficientBalanceException:
            print('user defined Exception')


            #print('Invaild Blance')
    def deoposit(self,cash):
        self.blance+=cash
        print('Current Blance is:',self.blance)

user1=Bank('balaji','12345')
user1.BlanceEnqury()
user1.deoposit(5000)
user1.withdraw(5000)
#user1.BlanceEnqury()
#user1.withdraw(4500)
#user1.BlanceEnqury()
------------------------------------------------

class InsufficientBlance(Exception):
    def __init__(self,mgs):
        self.mgs=mgs
        #print(self.mgs)

blance=1000
amount=int(input('Enter Your amount:'))

try:
    if amount>blance:
        raise InsufficientBlance('check your Balance')
#else:
#    print(amount)
except InsufficientBlance:
    print('Check your Blance!')
---------------------------------------------"""

