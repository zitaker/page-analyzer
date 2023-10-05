import psycopg2
import os

from flask import Flask
from flask import render_template
from flask import request
from psycopg2.extras import NamedTupleCursor
from flask import redirect
from flask import flash
# from .db import address_base_data


DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dergegkp20sdJUOIe3309f267jrthKfe42hrs'


with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
    curs.execute("CREATE TABLE url_checks (id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY, url_id bigint REFERENCES urls (id), status_code numeric, h1 text, title text, description text, created_at DATE NOT NULL DEFAULT CURRENT_TIMESTAMP);")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/urls/', methods=['POST'])
def page_urls():
    conn = psycopg2.connect(DATABASE_URL)
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

            if not ('http://' in get_request_form or 'https://' in get_request_form):
                flash('Некорректный URL', category='error')
                return redirect('/')

            if len(get_request_form) > 255:
                flash('URL превышает 255 символов', category='error')
                return redirect('/')

            curs.execute("INSERT INTO urls (name) VALUES (%s)", [get_request_form[:elem]])
            flash('Страница успешно добавлена', category='success')
            conn.commit()

            curs.execute('SELECT id FROM urls ORDER BY id DESC;', [id])
            row = curs.fetchmany(size=1)
            conn.close()

        for elem in row:
            return redirect(elem.id)


@app.route('/urls/<int:id>', methods=['GET', 'POST'])
def get_urls(id):
    conn = psycopg2.connect(DATABASE_URL)

    if request.method == ['GET'] or ['POST']:
        with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute("SELECT * FROM urls WHERE id = (%s)", [id])
            row = curs.fetchmany(size=1)

            curs.execute("SELECT * FROM url_checks WHERE url_id = (%s) ORDER BY id DESC", [id])
            url_id_row = curs.fetchall()
            # id == row

    if request.method == 'GET':
        return render_template('show.html', row=row, url_id_row=url_id_row)
    if request.method == 'POST':
        flash('Страница успешно проверена', category='success')

        with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute("INSERT INTO url_checks (url_id) VALUES (%s);", [id])
            curs.execute("SELECT * FROM url_checks WHERE url_id = (%s) ORDER BY id DESC", [id])
            url_id_row = curs.fetchall()
            conn.commit()
        conn.close()

        data_post = render_template('show.html', row=row, url_id_row=url_id_row)
        return data_post

# при повторном открытии существующего адреса после применения метота POST - сразу выводить данные из двух таблиц

@app.route('/urls', methods=['GET'])
def urls():
    conn = psycopg2.connect(DATABASE_URL)
    if request.method == 'GET':
        with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute("SELECT DISTINCT ON (urls.id) urls.id, urls.name, url_checks.created_at FROM urls FULL JOIN url_checks ON urls.id = url_checks.url_id ORDER BY urls.id DESC, created_at DESC;")
            rows = curs.fetchall()
            conn.close()
            return render_template(
            'urls.html', rows=rows)

    return render_template('urls.html')


@app.route('/process_data', methods=['POST'])
def button():
    if request.method == 'POST':
        return 'index'


@app.errorhandler(404)
def page_not_fount(error):
    return render_template('page_404.html', title='Страница не найдена')


if __name__ == '__main__':
    app.run()
