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

startN=1
tableN=int(input('Table Number:'))
endN=int(input('End Number:'))
while startN<=endN:
    print(f'{startN}*{tableN}={startN*tableN}')
    startN+=1
'''
