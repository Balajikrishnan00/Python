"""
# object -Class
class Student:
    '''This Class is about Students'''
print(Student.__doc__)

help(Student)
--------------------------------------------
class supermarket:
    '''This class is about supermarkets'''
#print(supermarket.__doc__)
#help(supermarket)
bread=supermarket()
bread.brand='abc'
print(bread.brand)
----------------------------------
items = []
while True:
    display = input('Press enter to continue.')
    print('------------------Welcome to the supermarket------------------')
    print('1. View items\n2. Add items for sale\n3. Purchase items\n4. Search items \n5. Edit items\n6. Exit')
    choice = input('Enter the number of your choice : ')

    if choice == '1' :
        print('------------------View Items------------------')
        print('The number of items in the inventory are : ',len(items))
        while len(items) != 0:
            print('Here are all the items available in the supermarket.')
            for item in items:
                for key, value in item.items():
                    print(key, ':', value)
            break

    elif choice == '2' :
        print('------------------Add items------------------')
        print('To add an item fill in the form')
        # while True:
        #     try:
        #         number_items = int(input('Enter the number of items you want to add in the inventory : '))
        #         break
        #     except ValueError:
        #         print('Number of items should only be in digits')
        # for num in range(number_items):
        item = {}
        item['name'] = input('Item name : ')
        while True:
            try:
                item['quantity'] = int(input('Item quantity : '))
                break
            except ValueError:
                print('Quantity should only be in digits')
        while True:
            try:
                item['price'] = int(input('Price $ : '))
                break
            except ValueError:
                print('Price should only be in digits')
        print('Item has been successfully added.')
        items.append(item)

    elif choice == '3' :
        print('------------------purchase items------------------')
        print(items)
        purchase_item = input('which item do you want to purchase? Enter name : ')
        for item in items:
            if purchase_item.lower() == item['name'].lower() :
                if item['quantity'] != 0 :
                    print('Pay ', item['price'] , 'at checkout counter.')
                    item['quantity'] -= 1
                else:
                    print('item out of stock.')

    elif choice == '4' :
        print('------------------search items------------------')
        find_item = input('Enter the item\'s name to search in inventory : ')
        for item in items:
            if item['name'].lower() == find_item.lower():
                print('The item named ' + find_item + ' is displayed below with its details')
                print(item)
            else:
                print('item not found.')

    elif choice == '5' :
        print('------------------edit items------------------')
        item_name = input('Enter the name of the item that you want to edit : ')
        for item in items:
            if item_name.lower() == item['name'].lower():
                print('Here are the current details of ' + item_name)
                print(item)
                item['name'] = input('Item name : ')
                while True:
                    try:
                        item['quantity'] = int(input('Item quantity : '))
                        break
                    except ValueError:
                        print('Quantity should only be in digits')
                while True:
                    try:
                        item['price'] = int(input('Price $ : '))
                        break
                    except ValueError:
                        print('Price should only be in digits')
                print('Item has been successfully updated.')
                print(item)
            else:
                print('Item not found')

    elif choice == '6' :
        print('------------------exited------------------')
        break

    else:
         print('You entered an invalid option')


---------------------------------


class supermarket:
    '''shiva organic supermarket'''

    def __init__(self, brand, price, discount=0):
        self.brand = brand
        self.price = price
        self.discount = discount



bread = supermarket('abc', 10, 2)
print(bread.price)
print(bread.discount)
# print(supermarket.__dict__)
shampoo = supermarket('xyz', 5, 1)
biscuit = supermarket('bb', 5, 3)

print(biscuit.__dict__)
--------------------------------
class math:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b

a1=math(10,20)
result=a1.addition()
print(result)
-----------------------------


class supermarket:
    '''shiva organic supermarket'''

    def __init__(self, brand, price, discount=0,total=0):
        self.brand = brand
        self.price = price
        self.discount = discount
        self.total=total

bread=supermarket('abc',10)
------------------------------
total=0
class supermarket:
    manufac='ssm'
    marketer='msm'
    def __init__(self,brand,price,discount=0):
        self.brand=brand
        self.price=price
        self.discount=discount
        #rice = supermarket('a1', 50)

    def order(self,quantity=0):

        self.quantity=quantity


    def bill(self):

        print(f'{self.brand }Quantity {self.quantity}\t\t:{self.quantity*self.price} SAR')
        return total

rice=supermarket('a1',50)
chilly=supermarket('aachi',30)
masala_items=supermarket('b2',35)
#print(rice.brand)
rice.order(2)
chilly.order(3)
masala_items.order(5)
rice.bill()
chilly.bill()
masala_items.bill()
----------------------------------------
# static variable
class supermarket:
    manufacturer='Ricemill' # class Variable
    marketer='SSM'          # class variable
    def __init__(self,brand,price):
        self.brand=brand # object variable
        self.price=price
rice=supermarket('A1',65)
masalaItems=supermarket('aachi',50)
------------------------------------------
class customer:
    def deposit(self,amt): # local variable
        print('You\'r going to deposit :',amt)
balaji=customer()

balaji.deposit(5000)
------------------------------------------
class t1:
    a=100
    def __init__(self):
        self.b=200
t=t1()
print(t.a)
print(t.b)
print(t1.a)
t.a=789
print(t.a)
print(t1.a)
t1.a=987
print(t1.a)
------------------------------------------
# type of methods

# 1. instance methods
# 2. class methods
# 3. static methods

class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def display(self):
        print('hi',self.name)
#s1=student('balaji',299)
#s1.display()
objectList=[]
for x in range(2):
    ob=input('Object:')
    na=input('Name:')
    ma=int(input('Mark:'))
    ob=student(na,ma)
    ob.display()
-----------------------------------"""
class office:
    noHolidays=10 # class variable

    @classmethod
    def checkHoliday(cls,branch,noHolidays=0):
        print('This year our ',branch,' has ',noHolidays)
        print('This year we have',cls.noHolidays)
        print()


#emp1=office()
#emp1.checkHoliday(15)
office.checkHoliday('chenai',12)
