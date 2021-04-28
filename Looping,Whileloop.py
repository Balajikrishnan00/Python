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
'''
