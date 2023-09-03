from flask import Flask
from flask import render_template

import psycopg2
import os

app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(dbname='database', user='postgres', password='postgres',
                                host='127.0.0.1', port='5432')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO urls (name) VALUES ('qwerty9')")
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('index.html')

    except:
        print('ошибка SQL. Can`t establish connection to database')


if __name__ == '__main__':
    app.run()
