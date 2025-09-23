from flask import Flask, render_template

app = Flask(__name__, static_folder='client/static/assets')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/upload")
def upload():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()