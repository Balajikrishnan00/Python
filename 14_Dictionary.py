# Dictionary
# key ,value Pair
# no duplicate key allowed
# value duplicate allowed
"""
timeTable={'Tamil':'10:00am','English':'12:00am','Maths':'10:00am'}
d={}
print(type(d))
for key in timeTable.keys():
    print(key)
    for value in timeTable.values():
        print(value)
d[1]='siva'
d[2]='shankar'
print(d)
print(d[1])
d[100]='balaji'
print(d)
# print(d[123]) Key Error
print(d.keys())
print(d.values())
del d[100]
print(d)
d.clear()
print(d)
del d
print(d)
------------------------------------
d={123:'balaji',124:'krishnan',125:'siva',126:'shankar'}
print(d)
d1={}
for x in range(5):

    key=input('enter Key:')
    value=input('enter Value:')
    d1[key]=value
print(d1)
--------------------------------------
d={123:'balaji',124:'krishnan',125:'siva',126:'shankar'}
print(len(d))
print(d.get(123))
print(d.get(211))
print(d[123])
print(d.pop(123))
print(d)
#print(d.pop(123)) # key Error

print(d.popitem())
print(d)
print(d.items())
-----------------------------
students={1:'balaji',3:'krishnan',6:'siva',2:'guru',7:'madhan',9:'ravi'}
marks1={1:[56,35,76,68,49],3:[46,72,61,42,63],6:[51,72,51,63,41],2:[52,62,72,61,51],7:[51,52,62,62,72],9:[42,42,41,41,53]}
marks2={1:{'Tamil':52,'English':45,'Maths':58,'Science':78,'Social':79},2:{'Tamil':62,'English':75,'Maths':88,'Science':98,'Social':79}}

#print(sorted(d.keys()))

#for key1 in students.keys():
#    for key2,value2 in marks1.items():
#        if key1==key2:
#            print(key1)
#            print(value2)
#for key,value in marks2.items():
#    print(key)
#    for key2,value2 in value.items():
#        print(f'{key2}\t:{value2}')
for item in students.items():
    print(type(item))
d1=students.copy()
print(d1)
print(id(d1))
print(id(students))
d2={}
d2.update(d1)
print(d2)
________________________________
d={'name':'balaji','age':25}
print(d.get('name'))
print(d.get('salary','Not Availble'))
print(d.get('salary',0))
----------------------------
#1
n=int(input('enter no of keys of dict:'))
d1={}
for i in range(n):
    key=input('Enter a key:')
    value=input('Enter a value:')
    d1[key]=value
print(d1)
---------------------------------"
#2
d=eval(input('Enter a key & value:'))
print(d) {'balaji':'krishnan'}
-----------------------------
d={}
while True:
   key=input('Key:')
   value=input('value:')
   y=input('Do you want to continuey/n:')
   d[key]=value
   if y=='y' or y=='Y':
       continue
   else:
       break
print(d)
--------------------------
# Error
superMarket={}
while True:
    itemCode=int(input('Enter item:'))

    #superMarket[itemCode]=
    key1=input('Enter key1')
    value1=input('Enter value1')
    key2=input('Enter key2:')
    value2=input('Enter value2')

    superMarket[itemCode]={key1[value1],key2[value2]}
    # superMarker={1108:{'brand':'kitkat','description':'made in italy'}
    ans=input('Do you want continue y/n:')
    if ans=='y':
        continue
    else:
        break
---------------------------------
product={'apple':100,'grapes':200,'banana':50,'orange':60}
discount=10 #%
#print(discount)
for key,value in product.items():
    #print(key,value-discount)
    #product[key]=product[key]
    dis=product[key]*10/100
    #product[key] = product[key]-dis
    product[key]=product[key]-(product[key]//10)


    #print(product[key])

print(product)
--------------------------------

product={'apple':100,'grapes':200,'banana':50,'orange':60}
#del product['apple']
#product.pop('apple')
print(product)
key=product.keys()

# Error
for x in key:
    if x=='apple':
        print(x)
        #print()
        del product[x]
print(product)
---------------------------"""
product={'apple':100,'grapes':200,'banana':50,'orange':60}
for key,value in product.items():
    if key=='grapes':
        del product[key]
        break# we

print(product)
