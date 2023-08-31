# import psycopg2
# import os
#
#
# DATABASE_URL = os.getenv('DATABASE_URL')
# print(DATABASE_URL)
# print('11111111111111111111')
# conn = psycopg2.connect(DATABASE_URL)
# print('22222222222222222222222222')
# print(conn)
# print('22222222222222222222222222')
#
# try:
#     # пытаемся подключиться к базе данных
#     conn = psycopg2.connect(dbname='database', user='postgres', password='postgres')
#     print('подключил SQL')
#     # conn = psycopg2.connect(DATABASE_URL)
#     # conn = psycopg2.connect('postgresql://postgres:postgres@host:port/database')
# except:
#     # в случае сбоя подключения будет выведено сообщение в STDOUT
#     print('Can`t establish connection to database')

import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
        print('работает')
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        print('не работает')
    return connection

conn = create_connection(
    "database", "postgres", "postgres", "127.0.0.1", "5432"
)


# # получение объекта курсора
# cursor = conn.cursor()
#
# # Получаем список всех пользователей
# cursor.execute('SELECT * FROM users')
# all_users = cursor.fetchall()
# cursor.close() # закрываем курсор
# conn.close() # закрываем соединение

