'''
name='welcome'
lenght=len(name) # len function using  no of charactor
print(name ,'=',lenght)

#Typecasting
# int()
print(int(123.45))
print(int(123.90))
print(int('123455'))


print(int(True))
print(int(False))

# float()
print(float(123))
print(float(True))
print(float(False))
print(float('123'))

#bool
print(bool(0))
print(bool(0.0))
print(bool(5))
print(bool(0.1))

#str()
print(str(10))
print(str(2.0))
print(str(True))
print(str(False))

#type() type ex int ,float,str,bool
# 14 data types available in python
no=100
name='shiva'
tamil=True
print(type(no))
print(type(name))
print(type(tamil))

# memory address
# id() memory address
a=10
b=20
c=10
print(id(a))
print(id(b))
print(id(c))

# immutable ,mutable
# cannot change,change of memory address
state1='TamilNadu'
state2='TamilNadu'
print(id(state1))
print(id(state2))
#2586639203440
#2586639203440

a=(10,20)
print(a)
for i in a:
    print(i)
    print(id(i))

# no constants in python
# convention full capital letter
# ex INTEREST_RATE=5

# Escape Characters
# \t - Tab
# \n - new line
# \' - single Qut

# operators
print(10+2)
print(10-4)
print(4*2)
print(9/3)
print(9//3)
print(20%3)
print(10**2)
print(10**3)

# Relational Operators
print(10>2)
print(10<3)
print(34<=12)
print(54>=21)

# equality operator
# chaining  operator
# == !=
print(10>30>90)
print(10<20>10)
# member ship operators
sen='God is Grace'
#1p
if 'God' in sen:
    print('True')
else:
    print('False')
#2p
names=['arun','ravi','siva','guna','mahesh']
if 'siva' in names:
    print('yes')
else:
    print('no')
#3p
no=[10,43,56,74,34,35,6,754,323,]
if 100 not in no:
    print('yes')
else:
    print('no')

# Ternary operator
#1p
a,b=21,20

c=30 if a>b else 40
print(c)

#2p
a=10
b=50
c=40

min =a if a<b and a<c else b

print(min)

#3P
a=int(input('Enter a value:'))
b=int(input('Enter b value:'))
c=int(input('Enter c value:'))

min=a if a<b and a<c else b if b<c else c
# min =a if  10<20 and 10<30
#        elif  20<30
#        else 30
max=a if a>b and a>c else b if b>c else c
print(min)
print(max)

#4p
a=int(input('A:'))
b=int(input('B:'))
c=int(input('C:'))
if a<b and a<c:
    min=a
    print(min)
elif b<c:
    min=b
    print(min)

else:
    min=c
    print(min)

# Identity Operator
# memory if location
# combine with memory location
a=12
b=23
print(a==b)
print(a is b)

name=input()
print('hi',name,'welcome to python world.')
print('hi'+name+'welcome to python world')
'''
named_list=[]
for i in range(5):
    name=input("enter name:")
    named_list.append(name)
print(named_list)


