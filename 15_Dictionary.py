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
--------------------------------

# binary search
l=[i for i in range(1,32)]
print(l)
for x in l:
    if x==31:
        print('yes')
        break
else:
    print('no')
-------------------------
# binary Search
# suitable for sorted
l=[1,2,3,4,5,6,13,14,15,16,9,10,11,12,18,19,20,21,22,23,24,17,7,8,25,26,27,28,29,30,31]
key=int(input("Enter your key:")) # 21
l2=sorted(l)
min=0
max=len(l2)-1
avg=min+max//2
#print(avg)
#print(avg)
print(l2)
while True:
    if key==l2[avg]:
        #print(avg)
        print('your number is present')
        break
    elif key<l2[avg]:
        #print(avg)
        max=avg-1
        avg=min+max//2
    else:
        #key>l2[avg]:
        #print(avg)
        min=avg+1
        avg=min+max//2
-------------------------
emp={'balaji':100,'kabilan':102,'Arun':103,'madhan':104}
emp2={}
empSalary={'balaji':10000,'kabilan':32000,'Arun':18000,'madhan':48000}
nameList=[]
salaryList=[]
for x,y in emp.items():
    emp2[y]=x
emp3={value:key for key,value in emp.items()}
print(emp2)
print(emp3)
for name,salary in empSalary.items():

    if salary>=25000:
        print(name)
for n in emp2.values():
    nameList.append(n)
print(nameList)

for salary in empSalary.values():
    salaryList.append(salary)
print(salaryList)

for salary in sorted(empSalary.values()):
    print(salary)
------------------------
# Bubble sort
l=[10,5,8,3]

#if l[0]>l[1]:
#    l[1],l[0]=l[0],l[1]
#if l[1]>l[2]:
#    l[1], l[2] = l[2],l[1]
#if l[2]>l[3]:
#    l[3],l[2]=l[2],l[3]
#print(l)
i=0
#while i<len(l)-1:

    #if l[i]>l[i+1]:
        #l[i+1],l[i]=l[i],l[i+1]
    #i+=1
#print(l)
while i<len(l)-1:
    j=i+1
    while j<len(l):
        if l[i]>l[j]:
            l[j],l[i]=l[i],l[j]
        j+=1
    i+=1
print(l)
-------------------------
l=[10,5,8,3]
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[j],l[i]=l[i],l[j]
        print(l)
------------------------------

interst=2
amount={'Balaji':1000,'Ragu':2200,'Dinesh':1300,'John':2200,'sathish':1500,'jarorld':100,"jonoto":50}
total=0
t2=0
Ins=0
print(f'NAME\t\tAmount\tInsterst\tTotalAmount')
print('--------------------------------------------')
for name,amou in amount.items():
    ins=amou*interst/100
    #print(ins)
    total=amou+ins

    print(f'{name}\t:\t{float(amou)}\t{ins}:\t{total}')
    #print('Total Amount')
    t2+=total
    Ins+=ins


    #total+=amou*(interst)/100

print('--------------------------------------------')
print(Ins,'Total:',t2,'SAR')
for val in sorted(amount.values()):
    print(val)
---------------------------------------"""
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
key=32
min=0
max=len(l)-1
#print(max)
avg=(min+max)//2
#print(avg)
while min<=max:
    if key==l[avg]:
        print('Key is preseht',key)
        break

    elif key>l[avg]:
        min=avg+1
        avg=(min+max)//2
    else:

        max=avg-1
        avg=(min+max)//2
else:
    print('KEY ERROR!...')
    #print('KEY is Not Found',key)