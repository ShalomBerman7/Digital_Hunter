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
        cursor.execute("""CREATE DATABASE IF NOT EXISTS c""")
        con.commit()
        log_event(level='INFO', message='exists/create database')

    except Exception as e:
        log_event(level='ERROR', message=e)


def create_table():
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS intel (
                        timestamp TIMESTAMP NOT NULL,
                        signal_id varchar(50) NOT NULL PRIMARY KEY,
                        entity_id varchar(15) NOT NULL,
                        reported_lat float NOT NULL,
                        reported_lon float NOT NULL,
                        
                        signal_type varchar(12) NOT NULL,
                        priority_level int(10) NOT NULL
                        )""")
        con.commit()
        log_event(level='INFO', message='exists/create table intel')

    except Exception as e:
        log_event(level='ERROR', message=e)


def insert_into(timestamp, signal_id, entity_id, reported_lat, reported_lon, signal_type, priority_level):
    try:
        cursor.execute("""INSERT INTO intel
                        (timestamp, signal_id, entity_id, reported_lat, reported_lon, signal_type, priority_level)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                       (timestamp, signal_id, entity_id, reported_lat, reported_lon, signal_type, priority_level))
        con.commit()
        log_event(level='INFO', message='inserted data to table intel')

    except Exception as e:
        log_event(level='ERROR', message=e)
