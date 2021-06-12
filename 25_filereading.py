"""
filename=input('Enter file name:')
if os.path.isfile(filename):
    print('file is present')
    file=open(filename,'r')
    lineCount=wordCount=charCount=0

    for line in file:
        lineCount+=1
    #print(lineCount)
        word=line.split()
        #print(word)
        wordCount+=len(word)
        #print(len(word))
        charCount+=len(word)
        for x in word:
            for y in x:
                charCount+=len(y)

    print(lineCount)
    print(wordCount)
    print(charCount)
------------------------------------------------------------------"""


class FileHandling:
    """This class is about FileHandling No of char,word and line """

    def __init__(self, fileName, fileMode):
        self.filename = fileName
        self.filemode = fileMode
        self.Line = self.Word = self.Char = 0

    def lineCount(self):
        with open(self.filename, self.filemode) as file:
            for l in file:
                self.Line += 1
        file.close()
        return self.Line

    def wordCount(self):
        with open(self.filename, self.filemode) as file:
            list1 = file.read()
        file.close()
        return len(list1.split())

    def charCount(self):
        with open(self.filename, self.filemode) as file:
            string = file.read()
        return len(string)


f1 = FileHandling('python.txt', 'r')
line = f1.lineCount()
print(line)
word = f1.wordCount()
print(word)
char = f1.charCount()
print(char)
print(FileHandling.__doc__)

if __name__ == '__main__':
    pass

