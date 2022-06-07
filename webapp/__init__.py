from flask import Flask
from flask import render_template
from webapp.catalog import catalog

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route("/")
    def index():
        key_db = app.config['DATABASE_API_KEY'] #заготовка для БД
        return render_template('index.html', catalog=catalog, key=key_db) #заготовка для БД

    return app