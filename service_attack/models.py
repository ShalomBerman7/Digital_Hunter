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
        con.commit()
        log_event(level='INFO', message='exists/create database')

    except Exception as e:
        log_event(level='ERROR', message=e)


def create_table():
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS attack (
                        timestamp TIMESTAMP NOT NULL,
                        attack_id varchar(50) NOT NULL PRIMARY KEY,
                        entity_id varchar(20) NOT NULL,
                        weapon_type varchar(20) NOT NULL,
                        )""")
        con.commit()
        log_event(level='INFO', message='exists/create table intel')

    except Exception as e:
        log_event(level='ERROR', message=e)


def insert_into(timestamp, attack_id, entity_id, weapon_type):
    try:
        cursor.execute("""INSERT INTO attack
                        (timestamp, attack_id, entity_id, weapon_type)
                        VALUES (%s, %s, %s, %s)""",
                       (timestamp, attack_id, entity_id, weapon_type))
        con.commit()
        log_event(level='INFO', message='inserted data to table intel')

    except Exception as e:
        log_event(level='ERROR', message=e)
