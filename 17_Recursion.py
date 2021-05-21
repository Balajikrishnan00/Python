"""
l=[1,3,5,7,9]
l1=[x*10+y for x in l for y in l]
print(l1)

------------------------------
def username(u,p):
    if u!='abcd':
        print('Incorrect Username')
        uName=input('UserName:')
        pWord=input('Password:')
        username(uName,pWord)
    elif p!='abcd':
        print('Incorrect Password')
        uName = input('UserName:')
        pWord = input('Password:')
        username(uName, pWord)
    else:
        print('welcome ')

uName=input('UserName:')
pWord=input('Password:')
username(uName,pWord)
-----------------------------
def dislplay(n):

    print(n)
    if n==10:
        pass
    n+=1
    if n<=996:
        dislplay(n)

dislplay(1)
---------------------------

def dis(n):
    print(n)
    n += 1
    if n<=5:
        dis(n)
#dis(1)
total=0
def ds(n):
    global total
    if n<=10:

        total+=n
        print(n)
        n+=1
        ds(n)

    else:
        print('total',total)
ds(1)
---------------
# factotial

def factorial(n):
    if (n==1 or n==0):
        return n
    else:
        #print(n)
        return n*factorial(n-1)



#v=int(input('Enter Possitive Factorial:'))
#len=len(str(factorial(100)))
#print(factorial(10))
#print(len)

# sum of digits
def sumofAdd(n):
    if n==1 or n==0:
        return n
    else:
        return n+sumofAdd(n-1)


print(sumofAdd(3))
---------------------
sum=0
n=12345
while n>=0:
    r=n%10  # 5,4,3,2,1
    sum+=r  # 0+5+4+3+2+1
    n=n//10 # 1234,123,12,1
print(sum)
------------------------
# sum of Digit

def SumOfDi(n): # 12345
    if n==0:
        return 0
    else:
        rem=n%10    # 5,4,3,2,1
        n//=10      # 1234,123,12,1,0
        return rem+SumOfDi(n)  # 1234,123,12,1
print(SumOfDi(12345))
--------------------------"""
