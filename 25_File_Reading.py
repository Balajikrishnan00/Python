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
------------------------------------"""
