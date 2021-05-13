"""
l1=[10,20,30,40,50,60,31,1201,1,32]
l1.sort()
print(l1)
#l1.reverse()
#print(l1)
#l1.sort(reverse=True)
#print(l1)
l1.reverse()
print(l1)
l2=l1
print(id(l2))
print(id(l1))
----------------------------
l1=[4,1,4,6,3,1]
l2=l1.copy()
print(id(l2))
print(id(l1))
l3=l2[:]
l4=l3[:]
l5=l2.copy()
print(l1)
print(l2)
print(l3)
print(l4)
print(id(l1))
print(id(l2))
print(id(l3))
print(id(l4))
print(id(l5))
---------------------------
l=[1,2,4,3,7,8,5,2]
#l.sort()
#l.sort(reverse=True)
#print(l)
#print(sorted(l,reverse=True))
print(l)
print(l[::-1])
------------------------
l1=[1,4,2,9,6]
l2=l1
l2[2]=22
print(l1)
print(l2)
-----------------------
l1=[1,5,2,7,8,5,3]
l2=l1.copy()
#print(l1,'\n',l2)
l2[2]=33
print(l1)
print(l2)
---------------------
l1=[1,7,3,2]
l2=l1[:]
#print(l1)
#print(l2)
l2[2]=45
print(l1)
print(l2)
---------------------
a=['balaji','krishnan']
b=['balaji','krishnan']
c=b

#print(a==b)
#print(a>b)
#print(a<b)
#print(a!=b)
#print(a is b)
#print(b is c)
print('balaji' in a)
print(c)
c.clear()
print(c)
----------------------
a=[[10,20,30],[40,50,60],[70,80,90]]
for x in a:
    for y in x:
        print(y,end=' ')
    print()

for x in a:
    print(x)
----------------------
a=[[10,20,30],[40,50,60],[70,80,90]]
for x in range(len(a)):
    print(a[x][x])
-----------------------"""

a=[[10,20,30],[40,50,60],[70,80,90]]
for i in range(len(a)):
    #print('index i',i)
    ll=a[i]
    for j in range(len(ll)):
        if i==j:
            print('index %i,%i :'%(i,j),end='')
        #print()

            print(a[i][j])

