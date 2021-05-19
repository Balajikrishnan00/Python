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
-------------"""
def calc(n1,n2):
    add=n1+n2
    sub=n1-n2
    mul=n1*n2
    div=n1/n2
    return add,sub,mul,div
print(calc(10,20))

