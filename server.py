from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/note', methods=['GET', 'POST'])
def note():
    return 'This is note page!'


if __name__ == '__main__':
    app.run(debug=True)