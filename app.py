import os
from dotenv import load_dotenv
import requests
from flask import Flask, request, render_template, url_for, send_from_directory, redirect
from utils.request_tools import __get_information
from utils.telegram_tools import send_telegram_message

load_dotenv()

app = Flask(__name__)
bot_token = os.getenv("TG_BOT_TOKEN")
move_group_id = os.getenv("TG_MOVE_GROUP_ID")
notify_group_id = os.getenv("TG_NOTIFY_GROUP_ID")


@app.route('/send-message', methods=['POST'])
def send_message():
    if request.method != 'POST':
        return

    message = f"""
🚀 We've got a request!
———————————
👤 Name: {request.form.get('person_name', 'Undefined')}
📱 Phone: {request.form.get('person_phone', 'Undefined')}
📱 Social Media teg: {request.form.get('contact-teg', 'Undefined')}
💬 Message: {request.form.get('person_note', 'Undefined')}
———————————
{__get_information(request)}
———————————
👨🏻‍💻 RiseApp Team
"""

    send_telegram_message(notify_group_id, message, bot_token)
    return redirect(url_for('index'))


@app.route('/')
def index():

    message = f"""
📈 We've detected a visitor! The main page.
———————————
{__get_information(request)}
———————————
👨🏻‍💻 RiseApp Team
"""

    send_telegram_message(move_group_id, message, bot_token)
    return render_template('index.html')


@app.route('/trendcity')
def project_1():

    message = f"""
📈 We've detected a visitor! The TrendCity page.
———————————
{__get_information(request)}
———————————
👨🏻‍💻 RiseApp Team
"""
    send_telegram_message(move_group_id, message, bot_token)
    return render_template('trendcity.html')


@app.route('/prolearn')
def project_2():

    message = f"""
📈 We've detected a visitor! The Prolearn page. 
———————————
{__get_information(request)}
———————————
👨🏻‍💻 RiseApp Team
"""
    send_telegram_message(move_group_id, message, bot_token)
    return render_template('prolearn.html')


@app.route('/skillpoint')
def project_3():

    message = f"""
📈 We've detected a visitor! The SkillPoint page. 
———————————
{__get_information(request)}
———————————
👨🏻‍💻 RiseApp Team
"""
    send_telegram_message(move_group_id, message, bot_token)
    return render_template('skillpoint.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
