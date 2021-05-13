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
---------------------------"""
