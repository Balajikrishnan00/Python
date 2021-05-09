# string is immutable
"""
name='Balajikrishnan'
print(name.find('i'))
----------------------
sen='python is very easy'
print(sen.count('y'))
print(sen.find('y',5,len(sen)+1))
-------------------------"""
sen='python is very easy'
c=0
for w in range(0,len(sen)):
    if sen[w]=='y':
        c+=1
print(c)

