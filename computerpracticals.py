import mysql.connector as myconnector
mycon = myconnector.connect(host="localhost", username="root", passwd="student", database="transport")
if mycon.is_connected():
    print("connection successful")
mycursor = mycon.cursor()
query = 'INSERT INTO STUDENT VALUES(5,"Amit", 78)'  
result = mycursor.execute(query)
mycon.commit()
