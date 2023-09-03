from flask import Flask
from flask import render_template
from .db import insert_into_urls


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html'), insert_into_urls()


if __name__ == '__main__':
    app.run()
