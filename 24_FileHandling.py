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
f=open('python.txt','w')
#f.write('balaji')
lis=['selvam','guru','ravi','siva']
for x in lis:
    f.write(x+' ')
------------------------
file=open('python.txt','w')
passwordList=['b','a','l','a','j','i']
for x in passwordList:
    for x in passwordList:
        file.write(x+x+'\n')
file.close()
---------------------
import re

#password = "R@m@_f0rtu9e$"
f1=open('python.txt','r')
data=f1.readline()
------------------------------------"""
