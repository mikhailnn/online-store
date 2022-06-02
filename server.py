from flask import Flask
from flask import render_template
from catalog import catalog

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template('index.html', catalog=catalog)

if __name__=="__main__":
    app.run(debug=True)