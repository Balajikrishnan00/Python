import mysql.connector
class Database:
    def __init__(self):
        print('Database Using:')
    def createDatabase(self,dbName):
        self.dbname=dbName
        db=mysql.connector.connect(host='localhost',user='root',password='root')
        crsr=db.cursor()
        query='CREATE DATABASE %s'
        value=(self.dbname,)
        crsr.execute(query,value)
        db.commit()
        db.close()
        print('Database Created')
    def DropDatabase(self,dbName):
        self.dbname=dbName
        db=mysql.connector.connect(host='localhost',user='root',password='root')
        crsr=db.cursor()
        query='DROP DATABASE %s;'
        value=(self.dbname,)
        crsr.execute(query,value)
        db.commit()
        db.close()
        print('Database Deleted')
    def ShowDatabase(self):
        db = mysql.connector.connect(host='localhost', user='root', password='root')
        crsr=db.cursor()
        query='SHOW DATABASES;'
        crsr.execute(query)
        res=crsr.fetchall()
        for x in res:
            print(x)

user1=Database()
user1.ShowDatabase()
user1.DropDatabase('pythondb')