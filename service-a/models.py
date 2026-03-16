import mysql.connector

con = mysql.connector.connect(user='user',
                              password='password',
                              host='localhost')

cursor = con.cursor()
cursor.execute("""CREATE DATABASE IF NOT EXISTS digital_hunter""")
