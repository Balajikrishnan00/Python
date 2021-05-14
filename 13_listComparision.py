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
---------------------------------"""
# list comprehension
l1=[i  for i in range(6) if i%2==0]
print(l1)

ll2=[val for val in l1 if val%2==0]
print(ll2)
ll3=[i for i in range(10)]
print(ll3)
ll4=[val for val in ll3 if val%2==0]
print(ll4)

