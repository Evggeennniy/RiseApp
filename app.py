import os
import uuid
import requests
from dotenv import load_dotenv
from flask import Flask, request, render_template, url_for, send_from_directory, redirect, make_response
from utils.request_tools import get_request_info
from utils.telegram_tools import send_telegram_message
from flask_babel import Babel, _

load_dotenv()

app = Flask(__name__)
bot_token = os.getenv("TG_BOT_TOKEN")
move_group_id = os.getenv("TG_MOVE_GROUP_ID")
notify_group_id = os.getenv("TG_NOTIFY_GROUP_ID")

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'


def get_locale():
    lang = request.args.get('lang')
    if not lang:
        lang = request.accept_languages.best_match(['ru', 'uk', 'en'])

    return lang


babel = Babel()
babel.init_app(app, locale_selector=get_locale)


@app.after_request
def after_request_handler(response):
    if request.path.startswith('/static') \
            or request.path.startswith('/favicon.ico') \
            or request.path.startswith('/send-message'):
        return response

    request_uuid = request.cookies.get('uuid')
    if not request_uuid:
        request_uuid = uuid.uuid4()
        response.set_cookie('uuid', str(request_uuid))

    request_info = get_request_info(request)

    log = f"""
📊 Cought a move by:
-------------------------------
🔗 Link: {request.url}
🆔 ID: {request_uuid}
🌍 IP: {request_info.get('user_ip')}
📌 Location: {request_info.get('user_location')}
🖥️ Device: {request_info.get('user_agent')}
-------------------------------
"""

    send_telegram_message(move_group_id, log, bot_token)

    return response


@app.route('/send-message', methods=['POST'])
def send_message():
    if request.method != 'POST':
        return

    request_info = get_request_info(request)

    log = f"""
🚀 Got a request by:
-------------------------------
👤 Name: {request.form.get('person_name', 'Undefined')}
📱 Phone: {request.form.get('person_phone', 'Undefined')}
📱 Email: {request.form.get('person_email', 'Undefined')}
💬 Message: {request.form.get('person_note', 'Undefined')}
-------------------------------
📊 About the request:
-------------------------------
🔗 Link: {request.url}
🆔 ID: {request.cookies.get('uuid')}
🌍 IP: {request_info.get('user_ip')}
📌 Location: {request_info.get('user_location')}
🖥️ Device: {request_info.get('user_agent')}
-------------------------------
👨🏻‍💻 RiseApp Team
"""
    send_telegram_message(notify_group_id, message, bot_token)
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html', lang=get_locale())


@app.route('/trendcity')
def project_1():
    return render_template('trendcity.html', lang=get_locale())


@app.route('/prolearn')
def project_2():
    return render_template('prolearn.html', lang=get_locale())


@app.route('/skillpoint')
def project_3():
    return render_template('skillpoint.html', lang=get_locale())


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
