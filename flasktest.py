from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'


@app.route('/<hash>', methods=['GET'])
def hash(hash = 0):
    return render_template('hash.html', hash=hash, params=range(5))


if __name__ == '__main__':
    app.run()