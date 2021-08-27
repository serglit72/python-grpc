#python_test.py
import mysql.connector


mydb = mysql.connector.connect(
  host = "mysql_af",
  user = "root",
  password="root",
  database = "anchorfree",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print("DATABASES : ", x)

mycursor.execute("SELECT us.id,us.user_name,us.traffic_limit,us.traffic_used,carr.id,carr.identity FROM user as us, carrier as carr where us.carrier_id = carr.id")
for t in mycursor:
	print(t)


mycursor.close()
mydb.close()