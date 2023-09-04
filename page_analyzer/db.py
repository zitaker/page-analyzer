import psycopg2
import os


DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)

def insert_into_urls():
    try:
        conn = psycopg2.connect(dbname='database', user='postgres', password='postgres',
                                host='127.0.0.1', port='5432')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO urls (name) VALUES ('qwerty33')")
        conn.commit()
        cursor.close()
        conn.close()

    except:
        print('ошибка SQL. Can`t establish connection to database')



