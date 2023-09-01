import psycopg2
import os


DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)

try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='database', user='postgres', password='postgres',
                            host='127.0.0.1', port='5432')
    print('подключил SQL')

except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')

cursor = conn.cursor()

# добавляем строку в таблицу people
cursor.execute("INSERT INTO urls (name) VALUES ('aida')")
# выполняем транзакцию
conn.commit()
print("Данные добавлены")

cursor.close()
conn.close()
        # import psycopg2
        # from psycopg2 import OperationalError
        #
        # def create_connection(db_name, db_user, db_password, db_host, db_port):
        #     connection = None
        #     try:
        #         connection = psycopg2.connect(
        #             database=db_name,
        #             user=db_user,
        #             password=db_password,
        #             host=db_host,
        #             port=db_port,
        #         )
        #         print("Connection to PostgreSQL DB successful")
        #         print('работает')
        #
        #
        #     except OperationalError as e:
        #         print(f"The error '{e}' occurred")
        #         print('не работает')
        #     return connection
        #
        # conn = create_connection(
        #     "database", "postgres", "postgres", "127.0.0.1", "5432"
        # )


# from psycopg2.extras import NamedTupleCursor
# with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
#     curs.execute('SELECT * FROM urls;')
#     # curs.execute('SELECT id, name, created_at  FROM urls WHERE name=%s', ('Bron',))
#     alfred = curs.fetchone()
#     print(alfred)

# cursor = connection.cursor()
#         postgres_insert_query = """ INSERT INTO urls (name)
#                                            VALUES (%s)"""
#         record_to_insert = ('qwerty')
#         cursor.execute(postgres_insert_query, record_to_insert)
#
#         connection.commit()
#         count = cursor.rowcount
#         print(count, "Запись успешно добавлена в таблицу urls")
