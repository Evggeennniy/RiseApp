import requests


def __send_telegram_message(chat_id, text, bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    print(url)
    requests.get(url, params={"chat_id": chat_id, "text": text})
    print(f"Message sent to {chat_id}")
