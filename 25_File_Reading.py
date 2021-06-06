"""
with open('python01.txt','r') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    # use Loop is good
----------------------
import os
#file='python01.txt'
if os.path.isfile('python01.txt'):
    print('Available')
_____________________________
import os
class fileHandling:
    '''this class is about File Handling'''
    def __init__(self,File):
        self.file=File
        self.read='r'
        if os.path.isfile(self.file):
            print('File is Available')
        else:
            print('File Does not Exist!')
    def fileLine(self):

        f=open(self.file,self.read)
        data=f.readlines()
        return len(data)
    def file_noof_word(self):

        self.word=0
        wordlist=[]
        f=open(self.file,self.read)
        data=f.readlines()
        for x in data:
            wordlist.append(x.split())
        for x in wordlist:
            for y in x:
                self.word+=1
        return self.word

    def No_of_char(self):
        f=open(self.file,self.read)
        data=f.readlines()
        char=0
        wordlist=[]
        for x in data:
            wordlist.append(x.split())
        for x in wordlist:
            for y in x:
                #print(list(y))
                for x in list(y):
                    for y in x:
                        if not y in ['.',',',':']:
                            char+=1
        return char


file1=fileHandling('python.txt')
print('No of line:',file1.fileLine())
print('No of word:',file1.file_noof_word())
print('No of char:',file1.No_of_char())
_______________
filename='python.txt'
file=open(filename,'r')
linecount=wordcount=charcount=0
for line in file:
    #print(line)
    #print(line)
    linecount+=1
    word=line.split()

    wordcount+=len(word)
    for x in word:
        for y in x:
            charcount+=len(y.split())
    #print(wordcount)

print(linecount)
print(wordcount)
print(charcount)
_______________________
filename='python.txt'
f=open(filename,'r')
l=w=c=0
for line in f:
    l+=1

    word=line.split()
    #print(word)
    w+=len(word)
    for x in word:
        c+=len(x)
print(l)
print(w)
print(c)
------------------------------------
import os
inputFile=open('C:/Users/balaj/Downloads/google.jpg','rb')
outputLoc=open('C:/Users/balaj/Downloads/goog.jpg','wb')

byte=inputFile.read()
outputLoc.write(byte)
---------------------------------------
import csv
c=len(dir(csv))
#print(c)
with open('student.csv','w',newline='')as f:
    pen=csv.writer(f)
    pen.writerow(['sid','sname','saddress'])
    students=int(input('Enter N of Student :'))
    for i in range(students):
        sid=input('Student Sid:')
        sname=input('student sname:')
        saddress=input('student Address:')
        pen.writerow([sid,sname,saddress])
--------------------------------------------
import csv
lis1=['balaji','siva','guru','men']
file=open('student.csv','a')
p=csv.writer(file)
p.writerow(lis1)
------------------------------------------
import csv
f1=open('python01.txt','r')
data=f1.readlines()
#print(len(data))
lis1=[]
for x in data:
    lis1.append(x.split())
f2=open('student.csv','w',newline='')
pen=csv.writer(f2)
for x in lis1:
    pen.writerow(x)
f2.close()
f1.close()
-----------------------------------"""
