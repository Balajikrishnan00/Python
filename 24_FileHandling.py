"""
file=open('python01.txt','w')
#print(file.name)
#print(file.mode)
#print(file.readable())
#print(file.writable())
#file.close()
#print(file.closed)
file.write('balaji\tKrishnan')
file.write('\n')
file.write('Python Developer')
file.close()
email_list=['garland@live.com','garland@optonline.net','psharpe@sbcglobal.net','starstuff@comcast.net','parrt@me.com']
f=open('python01.txt','w')
for x in email_list:
	f.write(x+'\n')
print('file writting Sucessfull')
f.close()
---------------------------------
import os
# r,w,a,r+,w+,a+,x

file=open('python01.txt','r')
print(file.name)
print(file.fileno())
print(file.mode)
#print(file.read())
word=file.read()
#print(type(word))
#print(word.count('c'))
file.close()
#print(word.title())
#print(file.writable())
#print(file.readable())
print(file.closed)
------------------------
f=open('python01.txt','r+')
data=f.readlines()
#print(data)
strdata=[]
for x in data:
    strdata.append(x.split())

print(len(strdata))
word=0
for i in strdata:
    word+=len(i)
    #for j in i:
        #print(j)
#print(word)
f.write('\nword='+str(word))
----------
f=open('python01.txt','r')
data=f.readlines()
data1=[]
for x in data:
    data1.append(x.split())
#print(data1)
str1=[]
for x in data1:
    for y in x:
        str1.append(list(y))
print(len(str1))
for x in str1:
    for y in x:
        if y=='.':
            with open('python.txt','a') as f2:
                f2.write(y)
                f2.close()
---------------------------------"""
# password Check Without Re
password=input('Please Enter Your Password:')
l1=list(password)
con1=False
con2=False
con3=False
con4=False
for x in l1:
    if x>='a' and x<='z':
        con1=True


    if x>='A' and x<='Z' :
        con2=True
    if x>='0' and x<='9' :
        con3=True
    if x in ['-','@','$']:
        con4=True
if con1 and con2 and con3 and con4:
    print(f'Your Password is Most Strong:')
else:
    print('Your Password is Week\nPlease Make it Strong')


