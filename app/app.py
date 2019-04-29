#!/bin/python
import MySQLdb
from MySQLdb import Error
import random
import string

HOST_DB = "dataBase"
PORT_DB = 3306
USER_DB = "user"
PASS_DB = "pass"

createDB = "CREATE DATABASE baseS3"
selectDB = "USE baseS3"
createTableDB = "CREATE TABLE users (id INT(5)AUTO_INCREMENT, user VARCHAR(10), name VARCHAR(10), address VARCHAR(30), PRIMARY KEY (id))"
showTable = "SELECT * FROM users"

def checkTableExists(myDB, tablename):
    cHandler = myDB.cursor()
    cHandler.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if cHandler.fetchone()[0] == 1:
        return True
    return False

try:
    myDB = MySQLdb.connect(host = HOST_DB, port = PORT_DB, user = USER_DB, passwd = PASS_DB)
    cHandler = myDB.cursor()
    ##cHandler.execute(createDB)
    cHandler.execute(selectDB)
    if checkTableExists(myDB, "users") == False:
        print ("Creating table: users")
        cHandler.execute(createTableDB)
    for i in range(1,11):
        cHandler.execute("INSERT INTO users (user, name, address) VALUES (user, name, address)")
        print("Added data to dataBase")
    cHandler.execute(showTable)
    myDB.commit()
except Error as e:
    print ("ERROR while connection to MySQL", e)
finally:
    myDB.close()
