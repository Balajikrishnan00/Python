"""
a=[9,1,8,2,7,3]
for i in range(len(a)):
    #print('I=',i)
    for j in range(i+1,len(a)):
        #print('J',j)
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
----------------------------------------
n=['balaji','arun','siva','guru','mathi']
a=[5,1,4,2,3]
for x in range(len(a)):
    for y in range(x+1,len(a)):
        if a[x]>a[y]:
            a[x],a[y]=a[y],a[x]
            n[x],n[y]=n[y],n[x]



print(a)
print(n)
---------------------------------
# list comprehension
l1=[i  for i in range(6) if i%2==0]
print(l1)

ll2=[val for val in l1 if val%2==0]
print(ll2)
ll3=[i for i in range(10)]
print(ll3)
ll4=[val for val in ll3 if val%2==0]
print(ll4)

names=['balaji','krishnan','siva','guru']
ll2=[names[0] for name in names]
print(ll2)

n1=[100,200,300,400]
m2=[500,400,600,200]
for x in n1:
    if x not in m2:
        print(x)
    #if x in m2:
    #    print(x)
n2=[x for x in n1 if x not in m2]
print(n2)
----------------------------------------
# Tuple
t=(10,20,30,40)
#print(type(t))
t1=(10)
#print(type(t1))
#print(t[1])
#print(t[100])
#print(t[::-1])
#t[1]=90 # Type Error
#print(t)
t2=(10,20,30)
t1=(5,15,25)
t3=t1+t2
#print(t3)
#print(len(t1))
#print(len(t1))

for x in range(len(t1)):
    print(t1[x],t2[x],end=' ')

print(type(sorted(t3)))
print(type(t3))
print(sum(t3))
print(min(t3))
print(max(t3))
-------------------------
a,b,c,d=10,20,30,40
t=a,b,c,d   # tuple packing

print(type(t))
print(t)
p,q,r,s=t # tuple unpacking
print(p,q,r,s)

print(a)
print(t[0])
print(p)
-------------------------

# tuple comprehension

l=(i for i in range(5))
print(type(l))

for i in l:
    print(i)
t=eval(input('Enter value'))
print(t)
for x in t:
    print(x)

--------------------------
l1=eval(input('enter a value:'))
for x in l1:
    if x%2==0:
        print(x)
---------------------------
#set
s={1,2,3,4,5,6,1}
print(s)
t=list(s)
print(t)
t=tuple(s)
print(t)
s1=set(t)
print(s1)
l1=[1,4,2,1,10]
s2=set(l1)
print(s2)

s3={i for i in range(10)}
print(s3)
s5=set(range(5))
print(s5)
s6=set()
print(type(s6))

for i in range(10):
    s6.add(i)
print(s6)
s6.add(2205)
print(s6)
s6.add('balaji')
print(s6)
s6.add(12)
print(s6)
s6.add('kri')
print(s6)
----------------------
l=[1,5,3,2]
s={'balaji','krishnan'}
#s.update(l)
#print(s)
s1=[100,500,1230,4250.3482,2842,42422]
s.update(s1,range(5))
print(s)
-------------------------
l=[i for i in range(1,11)]
t=(11,12,13,14)
print(l)
s={i for i in range(11,20)}
print(s)
print(t)
s.add(100)
s.update(t,l,range(20,25))
print(s)

for i in s:
    print(i)

print(len(s))
s2=s.copy()
print(s2)
print(type(s),id(s))
print(type(s2),id(s2))

#print(s[0])

print(s2.pop())
print(s2.pop())
#print(s.remove(1111))
#print(s)
s.discard(1111)
print(s)
s0={i for i in range(0,5) if i%2==0}
print(s0)
------------------------------
s={10,20,30,40,50}
s1={30,40,50}
#print(s.union(s1))
#print(s.intersection(s1))
print(s|s1)
print(s & s1)
print(s - s1)
print(s1 - s)
----------------------------"""