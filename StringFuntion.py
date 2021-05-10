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
-------------------------------
name='raja'
n1=name.replace('r','k')
#print(n1)
print(id(name.replace('r','m')))
print(id(name))
sen='your are not best'
sen2=sen.replace('not','the')
print(sen2)
-----------------------------
s='python is very easy'
#print(s.upper())
#print(s.lower())
#print(s.capitalize())
#print(s.title())
#print(s.swapcase())
#print(s[0].upper()+s[1:])
#print(s[::-1].upper())
Email=input('Enter Your Email:')


username=Email[:Email.index('@')]   # @gmail,@yahoo,@outlook,@hot
host=Email[Email.index('@')+1:Email.index('.com')]
length=len(username) #16
lower=[]
upper=[]
special=[]
number=[]
i=0

while i<length:
    if username[i]>='0' and  username[i] <='9': # for Number only Ex: 0 to 9
        number.append(username[i])

    elif username[i] >= 'a' and username[i] <= 'z': # Lowercase only
        lower.append(username[i])
    elif username[i]>='A' and  username[i] <='Z': # Uppercase only
        upper.append(username[i])
    else:
        special.append(username[i])
    i+=1
print('lower',lower)
print('upper',upper)
print('number',number)
print('special',special)
#user1=''.join(u1)
#print(user1)
#print(user1.lower())
#print(type(user1))
#print('Welcome! Mr.'+user1)
#print('Your Host is',host+'.com')

OP
Enter Your Email:balajiKrishnan123#$%@gmail.com
lower ['b', 'a', 'l', 'a', 'j', 'i', 'r', 'i', 's', 'h', 'n', 'a', 'n']
upper ['K']
number ['1', '2', '3']
special ['#', '$', '%']
--------------------------------------
s='balajikrishnan1234@gmail.com'
name=s[:s.index('@gmail')]
print(name)
print(s.index('@gmail'))
-----------------------------------
s1='python is very easy'
s2='python'
s3='1234567890'
#print(s.startswith('python'))
#print(s.endswith('python'))
#print(s.endswith('easy'))
#print(s.isalpha())
#print(s1.isalpha())
#print(s.isdigit())

# num
mobile='1234567890'
for let in mobile:
    if not (let>='0' and let<='9'):
        print('not')
        break
else:
    print('mob num')
-------------------------
# alpha
alphabet='balajikrishnan'
for l in alphabet:
    if not (l>='a' and l<='z'):
        print('not alpha')
        break
else:
    print('alpha')

------------------------
name=input('Enter Your Name \"Capital\":')
for l in name:
    if not (l>="A" and l<='Z'):
        print('Not in Capital!')
        break
else:
    print('Perfect')
    islower()
    isupper()

-----------------------"""
# formatting String
name='Raja'
salary=20000
age=55
print('my name is',name,'i am',age,'years old','my salary is RS',salary)
print('my name is %s i am %d years old my salary is RS%.2f'%(name,age,salary))
print('my name is {} i am {} years old my salary is RS{}'.format(name,age,salary))
print(f'my name is{name},i am {age} years old and my salary is RS{salary}')



