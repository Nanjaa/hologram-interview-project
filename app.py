import os

from flask import Flask, render_template
from flask_restful import Api

from hologram_project.api import CdrController

app = Flask(__name__, static_folder='client/static/assets')

# API set up with flask restful
api = Api(app)
api.add_resource(CdrController, '/cdr')

# DB connected with pymongo
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

# Routes
@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
