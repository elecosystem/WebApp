import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2250111",
    database="USER"
)


def insertData(self,name,uname,passwd,age):
    

INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');