import os
from dotenv import load_dotenv
import requests
from flask import Flask, request, render_template, url_for, send_from_directory, redirect

app = Flask(__name__)

load_dotenv()

admins_ids = [
    os.getenv("TEAMLEAD_ID"),
    os.getenv("ADMIN_ID")
]


def send_telegram_message(text):
    bot_token = os.getenv("TG_BOT_TOKEN")
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    for id in admins_ids:
        response = requests.get(url, params={"chat_id": id, "text": text})


@app.route('/send-message', methods=['POST'])
def send_message():
    if request.method != 'POST':
        return

    message = f"""
Получена заявка 💸
———————————
👤 {request.form.get('person_name')} 
📱 {request.form.get('person_phone')}
💬 {request.form.get('person_note', 'Без заметки')}
———————————
RiseApp Team 👨🏻‍💻
"""

    send_telegram_message(message)

    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/trendcity')
def project_1():
    return render_template('trendcity.html')


@app.route('/prolearn')
def project_2():
    return render_template('prolearn.html')


@app.route('/skillpoint')
def project_3():
    return render_template('skillpoint.html')


if __name__ == '__main__':
    app.run(debug=True)
