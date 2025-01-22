import os
from dotenv import load_dotenv
import requests
from flask import Flask, request, render_template, url_for, send_from_directory, redirect
from utils.request_tools import __get_information
# from utils.telegram_tools import send_telegram_message

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
🚀 Получена новая заявка!
———————————
👤 Имя: {request.form.get('person_name', 'Не указано')}
📱 Телефон: {request.form.get('person_phone', 'Не указано')}
📱 Соц. сеть: {request.form.get('contact-teg', 'Не указано')}
💬 Сообщение: {request.form.get('person_note', 'Не указано')}
———————————
{__get_information(request)}
———————————
👨🏻‍💻 RiseApp Team
"""

    # send_telegram_message(notify_group_id, message, bot_token)
    return redirect(url_for('index'))


@app.route('/')
def index():

    message = f"""
Движение на Главной странице.
———————————
{__get_information(request)}
———————————
👨🏻‍💻 RiseApp Team
"""

    # send_telegram_message(move_group_id, message, bot_token)
    return render_template('index.html')


@app.route('/trendcity')
def project_1():

    message = f"""
Движение на странице TrendCity.
———————————
{__get_information(request)}
———————————
👨🏻‍💻 RiseApp Team
"""
    # send_telegram_message(move_group_id, message, bot_token)
    return render_template('trendcity.html')


@app.route('/prolearn')
def project_2():

    message = f"""
Движение на странице Prolearn.
———————————
{__get_information(request)}
———————————
👨🏻‍💻 RiseApp Team
"""
    # send_telegram_message(move_group_id, message, bot_token)
    return render_template('prolearn.html')


@app.route('/skillpoint')
def project_3():

    message = f"""
Движение на странице SkillPoint.
———————————
{__get_information(request)}
———————————
👨🏻‍💻 RiseApp Team
"""
    # send_telegram_message(move_group_id, message, bot_token)
    return render_template('skillpoint.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
