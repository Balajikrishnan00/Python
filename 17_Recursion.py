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
---------------------------"""

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
