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

def insert_into_urls():
    cursor = conn.cursor()
    # добавляем строку в таблицу people
    cursor.execute("INSERT INTO urls (name) VALUES ('qwerty5')")
    # выполняем транзакцию
    conn.commit()
    print("Данные добавлены")
    cursor.close()
    conn.close()


# print(insert_into_urls())