# Database connection

import mysql.connector
from tabulate import tabulate

connection = mysql.connector.connect(host='localhost', user='root', password='root', database='pythondb')
cursor = connection.cursor()


def insert(name, age, city):
    sql = 'insert into users(name,age,city)values(%s,%d,%s)'
    user = (name, age, city)
    cursor.execute(sql, user)
    # cursor.execute('insert into users(name,age,city)values(%s,%i,%s);'%(name,age,city))
    connection.commit()
    print('Data Insert Successful.')


def update(name, age, city,id):
    sql = 'update user set name=%s,age=%d,city=%s where id=%s'
    user = (name, age, city, id)
    cursor.execute(sql, user)
    connection.commit()
    print('data update Successful')


def select():
    # cursor=connection.cursor()
    cursor.execute('Select * from users;')
    res = cursor.fetchall()
    print(tabulate(res, headers=['ID', 'NAME', 'AGE', 'CITY']))


def delete(id):
    pass

while True:
    print('1.Insert Database\t2.Update Database\t3.Select Database\t4.Delete ID\t5.Exit Database')
    choice = int(input('Enter Your Choice:'))

    if choice == 1:
        name = input('Enter NAME:').upper()
        age = int(input('Enter AGE:'))
        city = input('Enter CITY:').upper()
        insert(name, age, city)
    elif choice == 2:
        id = int(input('Enter ID:'))
        name = input('Enter NAME:').upper()
        age = int(input('Enter AGE:'))
        city = input('Enter CITY:').upper()
        update(name, age, city,id)
    elif choice == 3:
        select()
    elif choice == 4:
        id = int(input('Enter ID to Delete!'))
    elif choice == 5:
        quit()
    else:
        print('Invalid Selection!.')
