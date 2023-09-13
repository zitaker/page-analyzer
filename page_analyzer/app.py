import psycopg2
import os

from flask import Flask
from flask import render_template
# from .db import sql_connection
from flask import request
from psycopg2.extras import NamedTupleCursor

from flask import url_for, session, redirect
import json

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
            get_request_form = request.form.get('url')
            with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
                curs.execute("INSERT INTO urls (name) VALUES (%s)", [get_request_form])
                conn.commit()
                conn.close()
        except:
            print('ошибка SQL. Can`t establish connection to database')


@app.route('/urls/<int:id>')
def get_urls(id):
        conn = psycopg2.connect(dbname='database', user='postgres', password='postgres',
                                host='127.0.0.1', port='5432')
        with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute("SELECT * FROM urls WHERE id = (%s)", [id])
            row = curs.fetchmany(size=1)
            id == row

            conn.close()
        return f"{id} {row}"

# @app.route('/urls/<int:id>')
# def get_urls(id):
#     try:
#         conn = psycopg2.connect(dbname='database', user='postgres', password='postgres',
#                                 host='127.0.0.1', port='5432')
#         with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
#             curs.execute('SELECT * FROM urls ORDER BY id DESC;')
#             row = curs.fetchmany(size=1)
#
#             conn.close()
#
#     except:
#         print('ошибка SQL. Can`t establish connection to database')
#
#     return render_template('show.html', row=row), json.dumps(id)


@app.route('/urls', methods=['GET'])
def urls():
    if request.method == 'GET':
        try:
            conn = psycopg2.connect(dbname='database', user='postgres', password='postgres',
                                    host='127.0.0.1', port='5432')

            with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
                curs.execute('SELECT * FROM urls ORDER BY id DESC;')
                rows = curs.fetchall()
                conn.close()
                return render_template(
                'urls.html', rows=rows)

        except:
            print('ошибка SQL. Can`t establish connection to database')
    return render_template('urls.html')


@app.errorhandler(404)
def page_not_fount(error):
    return render_template('page_404.html', title='Страница не найдена')

if __name__ == '__main__':
    app.run()
