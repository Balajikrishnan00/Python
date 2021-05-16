"""
employees={'Balaji':100,'Krishnan':101,'Siva':102,'Madhan':103}
#print(employees)
employees2={}
for key,value in employees.items():
    employees2[value]=key
print(employees2)
for key in employees2.keys():
    print(key)
for value in employees2.values():
    print(value)
---------------------------------------------------
employees={'Balaji':100,'Krishnan':101,'Siva':102,'Madhan':103,105:'Guru'}
employee2={}
#for k,v in employees.items():
    #if k.isalpha():
    #    print(k.isalpha())
    #else:
    #    print(k)
e={v:k for k,v in employees.items()}
print(e)
---------------------------------------------
emp1={'balaji':10000,'krishnan':25000,'siva':3000}
emp2={}
name=[]
for key,value in emp1.items():
    emp2[value]=key
    name.append(key)
#    if value>=25000:
#        print(key)
#print(emp2)
#print(name)
for value in sorted(emp1.values()):
    print(value)
------------------------------------
l=[5,3,8,10]
i=0
while i<len(l)-3: # 0 ,1 ,2

    if l[i]>l[i+1]: # 0,0+1 ,1,1+2, 2,2+3
        l[i],l[i+1]=l[i+1],l[i]
    i+=1
print(l)
__________________________________
l=[10,5,8,3,7,1,9]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        #if l[i]>l[j]:
        print(i,j)

            #l[i],l[j]=l[j],l[i]

#print(l)
------------------------------------------
#product={'itemcode1':{'brandName':'ABX','MdfDate':'XXX','ExpDate':'YYY'},
#         'itemcode2':{'brandName':'ABX','MdfDate':'XXX','ExpDate':'YYY'},
#         'itemcode3':{'brandName':'ABX','MdfDate':'XXX','ExpDate':'YYY'}}

# bubble sort
l=[10,5,8,3,7,1,9]
i=0
print(l)
while i<len(l):
    j=1
    while j+i<len(l):
        if l[i]>l[j+i]:
            l[i],l[j+i]=l[j+i],l[i]
        j+=1
    i+=1
print(l)
---------------------------

l=[8,10,5,3,7,6]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[j],l[i]=l[i],l[j]
print(l)
---------------------------
l=[8,10,5,3,7,6]
i=0
while i<len(l):
    j=i+1
    while j<len(l):
        if l[i]>l[j]:
            l[j],l[i]=l[i],l[j]
        print(l)
        j+=1
    i+=1
print(l)
--------------------------
l1=[6,4,8,9,1]
i=0
while i<len(l1):
    print(i)
    j=i+1
    while j<len(l1):
        print('i:',i,end=(' '))
        print('j:',j)
        j+=1
    i+=1
    print()
----------------------------------
l=[10,20,30,40]
print(40 in l)
for x in l:
    if x==40:
        print('yes')
--------------------------------"""

# binary search
