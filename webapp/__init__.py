from flask import Flask
from flask import render_template
from webapp.queries import goods



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route("/")
    def index():        
        return render_template('index.html', catalogs=goods())
        
    return app