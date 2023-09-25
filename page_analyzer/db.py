import psycopg2
import os


DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)


def address_base_data():
    conn = psycopg2.connect(dbname='database', user='postgres', password='postgres',
                            host='127.0.0.1', port='5432')
    return conn

# def insert_into_urls():
#     try:
#         conn = psycopg2.connect(dbname='database', user='postgres', password='postgres',
#                                 host='127.0.0.1', port='5432')
#         cursor = conn.cursor()
#         # cursor.execute("INSERT INTO urls (name) VALUES ('qwerty33')")
#         cursor.execute("SELECT * FROM urls WHERE name = 'http://127.0.0.1:8000';")
#         # cursor.execute("SELECT * FROM urls;")
#         # already_exists_line = curs.fetchmany(size=1)
#         all_users = cursor.fetchmany(size=1)
#         # conn.commit()
#         cursor.close()
#         conn.close()
#         return all_users
#
#     except:
#         print('ошибка SQL. Can`t establish connection to database')
#
# print(insert_into_urls())



