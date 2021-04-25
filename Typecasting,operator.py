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
'''


