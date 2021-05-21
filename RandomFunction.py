import random
"""
for i in range(10):
    n=str(random.randint(100000,999999))
    OTP=(n[:3]+'-'+n[3:])
    print(OTP)
for i in range(20):
    m=random.randrange(10,99,2)
    print(m)

winnerList=['siva','selvan','balaji','bala']
for i in range(10):
    print(random.choice(winnerList))
"""
key=643894
n=0
while key !=n:

    n=random.randrange(100000,999999)
    print('Searching...')
    if key==n:
        print('well')
        print(f'Security Key:{key} Match Key:{n}')
        break

