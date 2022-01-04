import os
import datetime
import pymysql

#Get username from Clound9 workspace
username = os.getenv('C9_USER')

#Connect to the database

connection = pymysql.connect(host='localhost',
                            user = username,
                            password = '',
                            db = 'Chinook')
try:
    with connection.cursor() as cursor:
        cursor.execute("delete from Friends WHERE name = 'Bob';")
        connection.commit()
finally :
    #Close connection to (sql),regardless of whatever above was successful
    connection.close()