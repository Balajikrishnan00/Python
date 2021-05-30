"""
import Module1

res=Module1.sub(10,20)

print(res)

print(Module1.add(20,30))

from Module1 import add as a

#print(add(10,20))
res=a(20,20)
print(res)

import Module1
from Module1 import add,mul
from Module1 import *

print(Module1.mul(10,20))
print(mul(10,30))
print(add(50,50))


import Module1
#print(dir(Module1))

print(__name__)
#if __name__=='__main__':
#    pass
"""
import Module1
import cmath,math
print(__name__)
print(dir(cmath))
print(dir(math))
