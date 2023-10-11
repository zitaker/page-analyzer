import psycopg2
import os
import requests

# import re
import logging

from flask import Flask
from flask import render_template
from flask import request
from psycopg2.extras import NamedTupleCursor
from flask import redirect
from flask import flash
from bs4 import BeautifulSoup


DATABASE_URL = os.getenv('DATABASE_URL')
print(DATABASE_URL)


logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html')


def checking_indexes(curs, get_request_form):
    symbol = '/'
    indexes = [i for i, slash in enumerate(get_request_form)
               if slash == symbol]

    if len(indexes) < 3:
        elem = len(get_request_form)
    if len(indexes) > 2:
        elem = indexes[2]

    curs.execute(
        "SELECT id FROM urls WHERE name = (%s);",
        [get_request_form[:elem]]
    )
    already_exists_line = curs.fetchmany(size=1)
    return already_exists_line, elem


@app.route('/urls/', methods=['POST'])
def page_urls():
    conn = psycopg2.connect(DATABASE_URL)
    if request.method == 'POST':
        get_request_form = request.form.get('url').lower()

        with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
            already_exists_line, elem = checking_indexes(curs, get_request_form)

            for item in already_exists_line:
                flash('Страница уже существует', category='exists')
                return redirect(item.id)

            # condition = '[a-zA-Z0-9][.]([a-zA-Z]+){2}$'
            # condition_2 = '[a-zA-Z0-9][.]([a-zA-Z]+){2}[:]([0-9]+){2}$'
            # match = re.search(condition, get_request_form)
            # match_2 = re.search(condition_2, get_request_form)
            # if not (match or match_2):
            #     flash('Некорректный URL', category='error')
            #     return redirect('/')

            if not (get_request_form.startswith('http://')
                    or get_request_form.startswith('https://')):
                flash('Некорректный URL', category='error')
                return redirect('/')

            if len(get_request_form) > 255:
                flash('URL превышает 255 символов', category='error')
                return redirect('/')

            curs.execute(
                "INSERT INTO urls (name) VALUES (%s)",
                [get_request_form[:elem]]
            )
            flash('Страница успешно добавлена', category='success')
            conn.commit()

            curs.execute('SELECT id FROM urls ORDER BY id DESC;', [id])
            row = curs.fetchmany(size=1)
            conn.close()

        for elem in row:
            return redirect(elem.id)


def table_urls(conn, id):
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute("SELECT * FROM urls WHERE id = (%s)", [id])
        row = curs.fetchmany(size=1)

        curs.execute(
            "SELECT * FROM url_checks WHERE url_id = (%s) ORDER BY id DESC",
            [id]
        )
        url_id_row = curs.fetchall()
    return row, url_id_row


def parse(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    h1_tag = soup.find('h1')
    title_tag = soup.find('title')
    description_tag = soup.find('meta', attrs={'name': 'description'})

    h1 = h1_tag.text.strip() if h1_tag else ''
    title = title_tag.text.strip() if title_tag else ''
    description = description_tag['content'].strip() \
        if description_tag else ''
    return h1, title, description


@app.route('/urls/<int:id>', methods=['GET'])
def get_urls(id):
    if request.method == 'GET':
        conn = psycopg2.connect(DATABASE_URL)
        row, url_id_row = table_urls(conn, id)
        conn.close()
    return render_template('show.html', row=row, url_id_row=url_id_row)


@app.route('/urls/<int:id>', methods=['POST'])
def get_urls1(id):
    if request.method == 'POST':
        conn = psycopg2.connect(DATABASE_URL)
        row, url_id_row = table_urls(conn, id)
        with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute("SELECT * FROM urls WHERE id = (%s)", [id])
            row_name = curs.fetchmany(size=1)
            for elem in row_name:
                url = elem.name
                id_url = elem.id

            try:
                response = requests.get(url)
                status_code = response.status_code
            except:
                flash('Произошла ошибка при проверке', category='error')
                return redirect(id_url)

            h1, title, description = parse(url)

            curs.execute(
                "INSERT INTO url_checks"
                "(url_id, status_code, h1, title, description)"
                "VALUES (%s, %s, %s, %s, %s);",
                [id, status_code, h1, title, description]
            )
            curs.execute(
                "SELECT * FROM url_checks WHERE url_id = (%s) ORDER BY id DESC",
                [id]
            )

            url_id_row = curs.fetchall()
            conn.commit()
            flash('Страница успешно проверена', category='success')
            conn.close()

        data_post = render_template('show.html', row=row, url_id_row=url_id_row)
        return data_post


@app.route('/urls', methods=['GET'])
def urls():
    conn = psycopg2.connect(DATABASE_URL)
    if request.method == 'GET':
        with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
            curs.execute(
                "SELECT DISTINCT ON (urls.id) urls.id, urls.name, "
                "url_checks.created_at, "
                "url_checks.status_code FROM "
                "urls FULL JOIN url_checks ON "
                "urls.id = url_checks.url_id "
                "ORDER BY urls.id DESC, created_at DESC;")
            rows = curs.fetchall()
            conn.close()
            return render_template('urls.html', rows=rows)

    return render_template('urls.html')


@app.errorhandler(404)
def page_not_fount(error):
    return render_template('page_404.html', title='Страница не найдена')


if __name__ == '__main__':
    app.run()
