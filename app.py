from flask import Flask, render_template
from flask_restful import Api

from api import Cdr

app = Flask(__name__, static_folder='client/static/assets')
api = Api(app)
api.add_resource(Cdr, '/cdr')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/upload")
def upload():
    return render_template('upload.html')

@app.route("/list")
def list():
    return render_template('list.html')

if __name__ == '__main__':
    app.run()