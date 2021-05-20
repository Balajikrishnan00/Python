"""
def fun(name):
    print('hello Function',name)

#a1=input('Enter your Name:')
#fun(a1)
def sum(a,b):
    return int(a)+int(b)
v1=sum('1','2')
#print(v1)
def name(a='Gre'):
    print(a)
#name()
def squere(n):
    return n*n
def cube(n):
    return n*n*n
print(squere(5))
print(cube(5))

------------------------
def add(n,n1):
    return n+n1
print(add(10,20))
print(type(add(1,2)))
---------
def odd_even(n):
    if n%2==0:
        print('Even')
    else:
        print('odd')

#print(odd_even(5))
odd_even(5)
for i in range(10):
    odd_even(i)
-------------
def calc(n1,n2):
    add=n1+n2
    sub=n1-n2
    mul=n1*n2
    div=n1/n2
    return add,sub,mul,div
print(type(calc(10,20)))

t=10,20,30,40,50
print(t)
t1,t2,t3,t4,t5=t
print(t5)
----------------
def calc(n1,n2):
    add=n1+n2
    sub=n1-n2
    mul=n1*n2
    div=n1/n2
    return add,sub,mul,div
for x in calc(30,20):
    print(x)

------------------------
# types of Arguments
 # postional arguments
 # keyword arguments
 # dafalult arguments
 # variable arguments

# positional arguments
def add(n1,n2):
     pass

#add(10,20)

# keyword Arguments

def wish(name,mgs):
    print(f'Hi!,{name} {mgs}')
wish(name='balaji',mgs='welcome')



wish('balaji',mgs='HEllO')
#wish(mgs='greet','balaji')

#default argumets
def wish(mgs='HI!'):
    print(f'{mgs},balaji')
wish('welcome')
wish()
----------------
def discount(default=10):
    pass

def studentList(name):
    if name=='balaji' or name=='Balaji':
        print('Welcome',name)
        status=True
    else:
        print('Invaild Student Name!!!')

studentList('balaji')
------------------------
import random
def calculateTotal(*n):
    total=0
    for s in n:
        total+=s
    print(total)


for l in range(0,5):

    calculateTotal(random.randint(33,35))
-------------------------"""
def total(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
total(tamil=90,english=80,maths=87,social=78,science=58)
