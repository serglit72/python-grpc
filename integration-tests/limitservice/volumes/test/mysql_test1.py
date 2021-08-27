import mysql.connector
from mysql.connector import errorcode

try:
    mydb = mysql.connector.connect(host = "mysql_af",user = "root",password="root",database = "anchorfree",auth_plugin='mysql_native_password')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

cursor = mydb.cursor()

query = ("SELECT id,identity,traffic_limit_type,reset FROM carrier")

cursor.execute(query)

for (id,identity,traffic_limit_type,reset) in cursor:
     print("{}, {}, {}, {} ".format(id,identity,traffic_limit_type,reset))

cursor.close()
mydb.close()

# mydict = {}
# mydict1 = {} 
# json_key = ()
# json_value = ()

# cursor.execute(query)

# for row in cursor:
# 	json_key = row[1]
# 	json_value = row[2]
# 	# print("{}:{}".format(json_key,json_value))
# 	mydict[json_key] = json_value
# print(mydict)

# for row in cursor:
#     json_key = row[1]
#     json_value = row[3]
#     # print("{}:{}".format(json_key,json_value))
#     mydict1[json_key] = json_value
# print(mydict1)