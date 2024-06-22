from quart import Quart, send_from_directory

app = Quart(__name__)


@app.route('/')
async def index():
    return await send_from_directory('templates', 'index.html')


if __name__ == '__main__':
    app.run(debug=True)
