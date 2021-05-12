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
---------------------------"""
