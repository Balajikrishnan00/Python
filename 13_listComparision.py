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
-------------------------"""
a,b,c,d=10,20,30,40
t=a,b,c,d   # tuple packing

print(type(t))
print(t)
p,q,r,s=t # tuple unpacking
print(p,q,r,s)
