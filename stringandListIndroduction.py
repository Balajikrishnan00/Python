# merging two string
"""
s1=input('Enter s1 Name:')
s2=input('Enter s2 Name:')
s3=''

max=len(s1) if len(s1)>len(s2) else len(s2)
i=0
while i<max:
    if i<len(s1):
        s3+=s1[i]

    if i<len(s2):
        s3+=s2[i]
    i+=1
print(s3)
------------------------
alpha=''
dight=''
s='balajikrishnan123@gmail.com'
for l in s:
    if l.isalpha():
        alpha+=l
    if l.isdigit():
        dight+=l
print(alpha)
print(dight)
-------------------------
s=input('enter 1 char and 1 number ex(i*1):')

let=''

for l in s:
    if l.isalpha():
        let+=l
    if l.isdigit():
        n=int(l)
        print(let * n)
#print('balaji'*5)
#print(type('balaji'))
#print(type(let))
#print(let*n)
---------------------
# LIST=[]
groceryList=[]
print(type(groceryList))
print(id(groceryList))
groceryList.append('Red chilly')
print(id(groceryList))
markList=[55,34,56,78,96,43]
name='balajikrishnan'
n1=list(name)
n2=''.join(n1)
print(n2)
l2=list(range(5))
print(l2)
-------------------------
sen='python is very easy'.split()
date='30-12-2020'.split('-')
#print(sen[0][0])
#print(sen[1][0])
for x in date:
    print(x)
sen1='hi i am balajikrishnan'.split(' ')
c=0
for x in sen1:
    c+=1
print(c)
print(len(sen1))
----------------------------
lis1=[]
sen1='hi i am balaji'.split()
print(sen1)

for x in sen1:
    lis1.append(list(x))
print(lis1)
------------------"""
lis1=[['hi'],['i'],['am']]
print(lis1[1][0])
print(lis1[0][0])
print(lis1[2][0])
name='balajikrishnan'
lis2=[]
for n in name:
    lis2.append(n)

#print(name)
print(lis2)
print(lis2[::-1])


