import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='narayana@123',database='normal')
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE normal") 
mycursor.execute("SHOW DATABASES") 
mycursor.execute("CREATE TABLE Register(Name VARCHAR(255),Email VARCHAR(255),adress VARCHAR(255))") 
sql="INSERT INTO Register(Name,Email,adress)VALUES(%s,%s,%s)" 
val=("kiran","kiran@gmail.com","hyd")
mycursor.execute(sql,val)
mydb.commit()
mycursor.execute("SELECT * FROM Register") 
sql="SELECT * FROM Register WHERE adress='hyd'" 
sql="UPDATE Register SET adress='CHENNAI' WHERE adress='hyd'"
sql="SELECT * FROM Register LIMIT 5"
mycursor.execute(sql)
result=mycursor.fetchall()
for x in result:
    print(x)