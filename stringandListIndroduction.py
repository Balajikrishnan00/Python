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
-------------------------"""
s=input('enter 1 char and 1 number ex(i*1):')

let=''

for l in s:
    if l.isalpha():
        let+=l
    if l.isdigit():
        n=int(l)
#print('balaji'*5)
#print(type('balaji'))
#print(type(let))
print(let*n)





