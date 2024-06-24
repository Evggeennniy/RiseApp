from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/')
@app.route('/<string:lang>')
def index(lang='ru'):
    return send_from_directory('templates', f'index_{lang}.html')


if __name__ == '__main__':
    app.run(debug=True)
