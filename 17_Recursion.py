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
-----------------------------"""
