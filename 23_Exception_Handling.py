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
----------------------------------------"""
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