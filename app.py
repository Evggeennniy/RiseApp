from quart import Quart, send_from_directory

app = Quart(__name__)


@app.route('/')
@app.route('/<string:lang>')
async def index_eu(lang='ru'):
    return await send_from_directory('templates', f'index_{lang}.html')


if __name__ == '__main__':
    app.run(debug=True)
