'''
n=100
n1=n+10
print(n1)

# eval()
#1p
total=eval('10+20+30+40+50+60+70+80+90+100')
print(total)

#2p
total=eval(input("Enter total"))
print(total)

import math

print(math.pow(3,2))

# end= ,sep=
# formatted String
# %i - integer
# %d - integer
# %s string
# %f -float
name='siva'
age=24
weight=50.6
height=23
print('This is formatted string')

print('hi this is %s i am %i year old my height %d and weight %.2f.'%(name,age,height,weight))

print('hi this is {} i am {} year old my height {} and weight {}'.format(name,age,height,weight))

print(f'hi this is {name} i am {age} year old my height {height} and weight {weight}')
'''
# replacement Operator
name='Balaji'
city='Madurai'
print('This is {} from {}'.format(name,city))
print('This is {0} from {1}'.format(name,city))
print('This is {1} from {0}'.format(name,city))
print('This is {m} from {b}'.format(m=name,b=city))




