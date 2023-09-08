import psycopg2
import os

from flask import Flask
from flask import render_template
# from .db import sql_connection
from flask import request
from psycopg2.extras import NamedTupleCursor


DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/urls/', methods=['POST', 'GET'])
def page_urls():
    if request.method == 'POST':
        try:
            conn = psycopg2.connect(dbname='database', user='postgres', password='postgres',
                                    host='127.0.0.1', port='5432')
            cursor = conn.cursor()
            result = request.form.get('url')
            cursor.execute("INSERT INTO urls (name) VALUES (%s)", [result])
            conn.commit()
            cursor.close()
            conn.close()
            return render_template('show.html', result=result)
        except:
            print('ошибка SQL. Can`t establish connection to database')


@app.route('/urls', methods=['POST', 'GET'])
def urls():
    if request.method == 'GET':
        try:
            conn = psycopg2.connect(dbname='database', user='postgres', password='postgres',
                                    host='127.0.0.1', port='5432')

            # with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
            #     curs.execute("SELECT (id) FROM urls;")
            #     id_urls = curs.fetchall()
            # for i in range(len(id_urls)):
            #     id_atr = id_urls[i]

            with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
                curs.execute('SELECT * FROM urls ORDER BY id DESC;')
                rows = curs.fetchall()

                id_atr = []
                for row in rows:
                    id_atr.append((row[0]))

                name_atr = []
                for row in rows:
                    name_atr.append((row[1]))

                created_at_atr = []
                for row in rows:
                    created_at_atr.append((row[2]))

            conn.close()
            return render_template(
                'urls.html',
                id_atr=id_atr[0],
                name_atr=name_atr,
                created_at_atr=created_at_atr)
            # return render_template('urls.html', context={'all_users': all_users})


        except:
            print('ошибка SQL. Can`t establish connection to database')
    return render_template('urls.html')


if __name__ == '__main__':
    app.run()
