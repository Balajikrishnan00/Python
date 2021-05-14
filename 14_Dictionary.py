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
-----------------------------"""
