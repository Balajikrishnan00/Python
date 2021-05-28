class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def DoWork(self):
        print('Working')

print(dir(Human))
for x in dir(Human):
    if str(x):

        print(x,'string')
    elif dict(x):
        print('dict')

