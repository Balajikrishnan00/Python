'''
#1p multiples of 3
n1=3
s=1
while s<=10:
    print(n1,end=' ')
    n1+=3
    s+=1

#2p
count=20
n=3
while 1<=count:
    print(n,end=' ')
    n+=3
    count-=1

#3p
# 18,18,36,54,72,90,108,126
#5,5,10,15
i=18
sum1=[]
while i<=300:
    sum1.append(i)
    i+=18

print('')
i=5
sum2=[]
while i<=100:
    sum2.append(i)
    i+=5
print(sum1)
print(sum2)
l=0
for x in sum1:
    for y in sum2:
        if x==y:
            print(x)
#4p
# LCM
no1=2
no2=8
big =no1 if no1>no2 else no2
#print(big)

if big%no1==0 and big%no2==0:
    print('LCM ',big)

print('ji')

#5p
no1=int(input('Enter No1:'))
no2=int(input('Enter No2:'))
big=no1 if no1>no2 else no2

while True:
    if big%no1==0 and big%no2==0:
        print('LCM',big)
        break
    big+=1

#6p fact
n=5
fact=1
while n>0:
    fact*=n
    #print(fact)
    n-=1
print(fact)
'''
#7p Prime number

no=int(input('Enter a number:'))
i=2
while i<no:
    if no%i==0:
        print('not prime')
        break


    i+=1
else:
    print('prime')