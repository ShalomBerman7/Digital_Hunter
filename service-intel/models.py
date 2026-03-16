import mysql.connector
from shard.logger import log_event
import os

password = os.getenv('MYSQL_ROOT_PASSWORD', 'password')
con = mysql.connector.connect(user='user',
                              password=password,
                              host='localhost')

cursor = con.cursor()


def create_database():
    try:
        cursor.execute("""CREATE DATABASE IF NOT EXISTS digital_hunter""")
        log_event(level='INFO', message='create database')

    except Exception as e:
        log_event(level='ERROR', message=e)


create_database()
