# string is immutable
"""
name='Balajikrishnan'
print(name.find('i'))
----------------------
sen='python is very easy'
print(sen.count('y'))
print(sen.find('y',5,len(sen)+1))
-------------------------
sen='python is very very easy'
c=0
for w in range(0,len(sen)):
    if sen[w]=='y':
        print(w)
        c+=1
print(c)
-------------------------------"""
name='raja'
n1=name.replace('r','k')
#print(n1)
print(id(name.replace('r','m')))
print(id(name))
sen='your are not best'
sen2=sen.replace('not','the')
print(sen2)




