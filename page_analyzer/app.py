from flask import Flask
from flask import render_template
from .db import insert_into_urls
from flask import request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html'), insert_into_urls()


@app.route('/urls', methods=['POST', 'GET'])
def page_urls():
    if request.method == 'POST':
        result = request.form.get('url')
    return render_template('urls.html', result=result)


if __name__ == '__main__':
    app.run()
