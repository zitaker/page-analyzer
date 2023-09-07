import psycopg2
import os

from flask import Flask
from flask import render_template
# from .db import sql_connection
from flask import request


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
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM urls;")
            all_users = cursor.fetchall()

            cursor.close()
            conn.close()
            return render_template('urls.html', result1=all_users)


        except:
            print('ошибка SQL. Can`t establish connection to database')
    return render_template('urls.html')

if __name__ == '__main__':
    app.run()
