"""
#no=64
no='A5'
#print(chr(no+1))
no2=int(no[1])+65
#print(chr(no2))
print(no2)
no3=no[0]+chr(no2)
print(no3)
----------------------------
lis1=[10,20,30,130,20,30,34]
c=0
for x in lis1:
    if x==20:
        c+=1
#print(c)
#print(lis1.count(20))
-----------------------------
import random
lis=[]
for x in range(1,20):
    lis.append(random.randint(1,50))
#print(lis)
----------------------------
lis=[1,42,53,23,12,43,12,45,23,23,12]
#print(lis.index(12))

# manipulation
lis.append(500)
lis.append(400)
print(lis)
----------------------------
lis=[]
for x in range(1,5+1):
    lis.append(x)
print(lis)
------------------------------
lis=[]
for x in range(1,11):
    if x%2==0:
        lis.append(x)
print(lis)
----------------------------
lis=[]
for x in range(1,11):
    if x%2==0:
        lis.append(x*x)
print(lis)
---------------------------
l=[1,3,4,3,5,6,7,8,9]
l.insert(3,50)
print(l)
-------------------------
l1=[1,2,3,4,5,6,7,8,9,0]
l2=['a','b','c','d']
l1.extend(l2)
print(l1)
print(l2)
l2.extend(l1)
print(l2)
l3=[1,2,3,4]
l3.extend(l3)
print(l3)
l4=[]
l4.extend('Balaji')
print(l4)
-----------------------
l=[]
l.extend('balaji')
print(l)
l.extend([1,2,3,4,5])
print(l)
l.remove(1)
print(l)
l.pop(2)
print(l)
l1=[]
l1.append('balaji')
print(l1)
l1.extend('balaji')
print(l1)
l1.pop()
print(l1)
print(l1.pop())
print(l1)
l1.pop(1)
print(l1)
---------------------------
l=[10,20,30,40,60,50]
#l.reverse()
print(l)
print(l[::-1])
len=len(l)-1
i=0
l1=[]
while len>=i:
    l1.append(l[len])
    len-=1
print(l1)
------------------------------
name=input('Enter a name:')
l1=[]
l2=[]
l1.extend(name)
#print(l1)
i=len(l1)-1
while i>=0:
    l2.append(l1[i])
    i-=1
print(l1)
print(l2)
----------------------------
name='balaji'
l2=[]
l1=list(name)
#print(l1)
for x in range(0,len(l1)):
    l2.append(l1.pop())
l1=l2
print(l1)
print(l2)
--------------------------
sen='i am balaji krishnan'
l1=sen.split()
print(l1)
print(l1[::-1])
i=len(l1)-1

while i>=0:
    #print(l1[i])
    y=len(l1[i])-1
    while y>=0:
        print(l1[i][y],end='')
        y-=1
    #print(y)
    #while
    print()
    i-=1
#   ['i', 'am', 'balaji', 'krishnan']
#   ['krishnan', 'balaji', 'am', 'i']
#   nanhsirk
#   ijalab
#   ma
#   i
-------------------------"""
sen='wish you a very happy New year'
l1=list(sen)
l2=sen.split()
l3=[]
print(l1)
print(l2)
# 1 method - print(l2[::2])
i=0
#2 method -
while i<=len(l2)-1:
    if i==0 or i%2==0:
        l3.append(l2[i][::-1])
    else:
        l3.append(l2[i])

    i+=1
print(l3)
