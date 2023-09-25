import psycopg2
import os

from flask import Flask
from flask import render_template
from flask import request
from psycopg2.extras import NamedTupleCursor
from flask import redirect
from flask import flash
from .db import address_base_data

DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dergegkp20sdJUOIe3309f267jrthKfe42hrs'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/urls/', methods=['POST'])
def page_urls():
    conn = address_base_data(DATABASE_URL)
    if request.method == 'POST':
        get_request_form = request.form.get('url')

        symbol = '/'
        indexes = [i for i, slash in enumerate(get_request_form) if slash == symbol]

        if len(indexes) < 3:
            elem = len(get_request_form)
        if len(indexes) > 2:
            elem = indexes[2]

        with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute("SELECT id FROM urls WHERE name = (%s);", [get_request_form[:elem]])
            already_exists_line = curs.fetchmany(size=1)
            for item in already_exists_line:
                flash('Страница уже существует', category='exists')
                return redirect(item.id)

            curs.execute("INSERT INTO urls (name) VALUES (%s)", [get_request_form[:elem]])
            if 'http://' in get_request_form or 'https://' in get_request_form:
                flash('Страница успешно добавлена', category='success')
                conn.commit()
            else:
                flash('Некорректный URL', category='error')
                return redirect('/')

            curs.execute('SELECT id FROM urls ORDER BY id DESC;', [id])
            row = curs.fetchmany(size=1)
            conn.close()

        for elem in row:
            return redirect(elem.id)


@app.route('/urls/<int:id>', methods=['GET'])
def get_urls(id):
    conn = address_base_data(DATABASE_URL)
    if request.method == 'GET':
        with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute("SELECT * FROM urls WHERE id = (%s)", [id])
            row = curs.fetchmany(size=1)
            id == row
            conn.close()

    return render_template('show.html', row=row)


@app.route('/urls', methods=['GET'])
def urls():
    conn = address_base_data(DATABASE_URL)
    if request.method == 'GET':
        with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute('SELECT * FROM urls ORDER BY id DESC;')
            rows = curs.fetchall()
            conn.close()
            return render_template(
            'urls.html', rows=rows)

    return render_template('urls.html')


@app.errorhandler(404)
def page_not_fount(error):
    return render_template('page_404.html', title='Страница не найдена')


if __name__ == '__main__':
    app.run()

