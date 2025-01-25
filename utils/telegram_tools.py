import requests


def send_telegram_message(chat_id, message, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    respond = requests.get(url, params={"chat_id": chat_id, "text": message})
