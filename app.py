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


def get_client_ip():
    """Функция для получения IP-адреса клиента, даже если он за прокси"""
    ip = request.headers.get('X-Forwarded-For', request.headers.get('X-Real-IP', request.remote_addr))

    # Если клиент за прокси, X-Forwarded-For может содержать список IP через запятую
    if ip and "," in ip:
        ip = ip.split(",")[0].strip()  # Берем первый IP из списка

    return ip


def get_ip_info(ip):
    """Функция для получения информации о местоположении IP (через IP-API)"""
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?lang=ru")
        data = response.json()
        if data["status"] == "success":
            return f"{data['country']} 🇦🇷, {data['regionName']} 📍, {data['city']} 🌆"
        else:
            return "Не удалось определить местоположение 🌍"
    except Exception:
        return "Ошибка при определении местоположения 🚨"


def send_telegram_message(text):
    bot_token = os.getenv("TG_BOT_TOKEN")
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    for id in admins_ids:
        response = requests.get(url, params={"chat_id": id, "text": text})


@app.route('/send-message', methods=['POST'])
def send_message():
    if request.method != 'POST':
        return

    ip_address = get_client_ip()
    location = get_ip_info(ip_address)

    user_agent = request.headers.get('User-Agent', 'Неизвестно 🤷‍♂️')

    message = f"""
🚀 Получена новая заявка!
———————————
👤 Имя: {request.form.get('person_name', 'Не указано')}
📱 Телефон: {request.form.get('person_phone', 'Не указан')}
💬 Сообщение: {request.form.get('person_note', 'Без заметки')}
———————————
📊 Сведения об отправителе:
🌍 IP: {ip_address}
📌 Местоположение: {location}
🖥️ Устройство: {user_agent}
———————————
👨🏻‍💻 RiseApp Team
"""

    send_telegram_message(message)  # Отправка в Telegram

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
    app.run(debug=False, host='0.0.0.0', port=5000)
