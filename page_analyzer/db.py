import psycopg2
import os

# from dataclasses import dataclass


DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)


# def address_base_data():
#     conn = psycopg2.connect(dbname='database', user='postgres', password='postgres',
#                             host='127.0.0.1', port='5432')
#     return conn
# print(address_base_data())


# @dataclass
# class address_base_data:
#     dbname: str
#     user: str
#     password: str
#     host: str
#     port: str

    # def __init__(self, dbname, user, password, host, port):
    #     self.dbname = dbname
    #     self.user = user
    #     self.password = password
    #     self.host = host
    #     self.port = port

    # def method(self):
    #     conn = psycopg2.connect(self.dbname, self.user, self.password,
    #                         self.host, self.port)
    #     return conn

# address_base_data = address_base_data('database', 'postgres', 'postgres', '127.0.0.1', '5432')
# print(address_base_data)


# class address_base_data(object):
#     if os.getenv('DATABASE_URL'):
#         SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://", 1)
#     else:
#         SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASEDIR, 'instance', 'app.db')}"


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
