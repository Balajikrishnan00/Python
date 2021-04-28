'''
# Iterative statements
#1p
i=0
while i<5:

    print(i,end=' ')
    i+=1

#2p
i=1
while i<=5:
    print(i,end=' ')
    i+=1

#3p
i=0
e=int(input('Range value:'))
while i<=e:
    print(i,end=' ')
    i+=1

#4p
i=5
while i>=0:
    print(i,end=' ')
    i-=1

#5p
i=10
while i>=0:
    print(i,end=' ')
    i-=2

#6p
i=2
while i<=100:
    print(i,end=' ')
    i+=2

#7p
i=1
while i<=100:
    print(i,end=' ')
    i+=2

#8p
i=3
while i<=100:
    print(i,end=' ')
    i*=3

#9p
sNumber=1
eNumber=int(input('End value:'))
while sNumber<=eNumber:
    if sNumber%3==0:
        print(sNumber,end=' ')
    sNumber+=1

#10p
startN=1
tableN=int(input('Table Number:'))
endN=int(input('End Number:'))
while startN<=endN:
    print(f'{startN}*{tableN}={startN*tableN}')
    startN+=1

#11p
sN=6
eN=100
while sN<=eN:
    print(sN,end=' ')
    sN+=6

#12p
sn=1
en=100
while sn<=en:
    if sn%2==0 and sn%3==0:
        print(sn,end=' ')
    sn+=1
#13p
s=1
e=100
while s<=100:
    if s%2==0 or s%3==0:
        print(s,end=' ')
    s+=1


#14p
box=0
firstDay=1
lastDay=365
amount=0
while firstDay<=lastDay:
    amount+=1
    box=box+amount
    print('day%d amount=%d total=%d'%(firstDay,amount,box))
    firstDay+=1

#15p
# addition of n numbers
i=0
n=int(input('Enter n number:'))
sum=0
while i<=n:
    sum+=i
    i+=1
print(sum)

#16p
name=input('what is your name:')
print(len(name))


#17p
name=input('name:')
i=0
while i<len(name):
    print(name[i])
    i+=1

#18p
name='saiva'
i=0
while i<len(name):
    if name[i]=='a':
        print(name[i])
    i+=1


#19p

name='rajarajan kumar'
print(name.count('a'))

#20p
name='rajarajan kumar'
i=0
count=0
while i<len(name):
    if name[i]=='a':
        count+=1
    i+=1
print(count)

#21p
n=0
while n<=10:
    n+=1
    if n==5:
        break
    print(n)

#22p
n=0
while n<=10:
    n+=1
    if n==5:
        continue
    print(n)

#23p
name=input('Enter a name:')
vow=['a','e','i','o','u']
for i in name:
    for j in vow:
        if j==i:
            print('vowvels')

#24p
name=input('Name:')
vow=['a','e','i','o','u']
i=0
while i<len(name):
    if name[i] in vow:
        print(name[i],'vow')
    i+=1

#25p
name=input('Name:')
vow=['a','e','i','o','u']
i=0
while i<len(name):
    if name[i] not in vow:
        print(name[i],'not vow')
    i+=1
'''
#26p
name=input('Name:')
i=0
count=0

while i<len(name):
    if name[i] in ['a','e','i','o','u']:
       count+=1
    i+=1
print(count)

