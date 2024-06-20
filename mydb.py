import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
)
#prepare a curdsor object
cursorObject=dataBase.cursor()
#creatte a database 
cursorObject.execute("CREATE DATABASE AdityaDb")
print("All done")
