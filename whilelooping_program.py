'''
#1p multiples of 3
n1=3
s=1
while s<=10:
    print(n1,end=' ')
    n1+=3
    s+=1
---------------------------------
#2p
count=20
n=3
while 1<=count:
    print(n,end=' ')
    n+=3
    count-=1
----------------------------------
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
-----------------------------
#4p
# LCM
no1=2
no2=8
big =no1 if no1>no2 else no2
#print(big)

if big%no1==0 and big%no2==0:
    print('LCM ',big)

print('ji')
----------------------------------
#5p
no1=int(input('Enter No1:'))
no2=int(input('Enter No2:'))
big=no1 if no1>no2 else no2

while True:
    if big%no1==0 and big%no2==0:
        print('LCM',big)
        break
    big+=1
-----------------------------------
#6p fact
n=5
fact=1
while n>0:
    fact*=n
    #print(fact)
    n-=1
print(fact)
-----------------------------------
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
-----------------------------------
# Reverse string
#8.1P
no=123345678

no=str(no)
print(type(no))

no=int(no[::-1])
print(int(no))
print(type(no))
----------------------------------------
# 8.2 p
no=1234
numbers=str(no)
i=len(numbers)-1
while i>=0:
    print(numbers[i],end='')
    i-=1
----------------------------------
# 9.1 sum of Digit


no= '1234' #input('Enter a number:')
sum=0
i=len(no)-1
while i>=0:
    print(no[i])
    i-=1
    sum=sum+int(no[i])
print(sum)
------------------------------------
# palindrome

s=input('Enter a string:')

s1=s[::-1]
if s==s1:
    print('Palindrome')
else:
    print('Not Palindrome')
--------------------------------------
# reverse number
no=1234
c=0
while no>0:
    print(no%10)
    no//=10
    c+=1
print(c)
------------------------------------------'''
# adition of digits

no=int(input('Enter a Number'))
count=0
sum=0
while no>0:
    d=no%10
    sum+=d
    no//=10
    count+=1
print('Sum of Add Digits %i '%sum)
print('count of Digits %i'%count)

