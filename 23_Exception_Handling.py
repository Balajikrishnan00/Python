try:
    no1 = int(input('Enter No1:'))
    no2 = int(input('Enter No2:'))
    print(no1 / no2)
except ZeroDivisionError:
    print('Zero division Error')
finally:
    print('Welcome to Balaji')
    