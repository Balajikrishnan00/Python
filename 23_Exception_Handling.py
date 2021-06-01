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
-------------------------------------------"""
# finally

try:
    print('Hi')
except SyntaxError:
    print('Welcome')
finally:
    print('good')


# os.exit() will not use finally