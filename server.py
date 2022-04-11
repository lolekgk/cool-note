from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_page():
    return 'This is the main page!'


@app.route('/note', methods=['GET', 'POST'])
def note():
    return 'This is note page!'
