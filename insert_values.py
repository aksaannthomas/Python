import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"

)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Aksa", "Kochi")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
