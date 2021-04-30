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
'''
