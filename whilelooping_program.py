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
------------------------------------------
# sum of digits

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
------------------------------------
no=1221
n1=no
reverse=0
sumofDigits=0
count=0
while no>0:
    r=no%10
    reverse=reverse*10+r
    sumofDigits=sumofDigits+r
    no=no//10
    count+=1
if n1==reverse:
    print('Palindrome ')
else:
    print('not Palindrome')
print('The Number is %i'%n1)
print('reverse %i'%reverse)
print('Sum Of Digits %i'%sumofDigits)
print('Count of Digit %i'%count)
----------------------------------
# Armstrong number
import math
no=int(input('Enter Armstrong number:'))
n1=no
sum=0

while no>0:
    r=no%10
    n=int(math.pow(r,3))
    no//=10
    sum=sum+n
if n1==sum:
    print('Armstrong number')
else:
    print('Not Armstrong Number')
-------------------------------------
#  abcd... = an + bn + cn + dn + ...
num=153
pow=len(str(num))
n1=num
ams=0
while num>0:
    r=num%10
    ams=ams+r**pow
    num=num//10
if n1==ams:
    print('Ams')
else:
    print('Not Ams')
------------------------ '''
n=81
n1=n
pow=len(str(n))
sum=0
n3=0
while n>0:
    r=n%10
    sum=sum+r

    n=n//10
    n3=sum**pow
if n1==n3:
    print('n1=%i n3=%i'%(n1,n3))

