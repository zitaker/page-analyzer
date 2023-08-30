import psycopg2
import os

DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)

try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='database', user='postgres', password='postgres')
    # conn = psycopg2.connect(DATABASE_URL)
    # conn = psycopg2.connect('postgresql://postgres:postgres@host:port/database')
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')

