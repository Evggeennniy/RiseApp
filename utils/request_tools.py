import requests


def __get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?lang=ru")
        data = response.json()
        if data["status"] == "success":
            return f"{data['country']} 🇦🇷, {data['regionName']} 📍, {data['city']} 🌆"
        else:
            return "Не удалось определить местоположение 🌍"
    except Exception:
        return "Ошибка при определении местоположения 🚨"


def __get_client_ip(request):
    """Функция для получения IP-адреса клиента, даже если он за прокси"""
    ip = request.headers.get('X-Forwarded-For', request.headers.get('X-Real-IP', request.remote_addr))

    if ip and "," in ip:
        ip = ip.split(",")[0].strip()

    return ip


def __get_information(request):
    ip_address = __get_client_ip(request)
    location = __get_ip_info(ip_address)
    user_agent = request.headers.get('User-Agent', 'Неизвестно 🤷‍♂️')

    message = f"""
📊 Сведения об отправителе:
🌍 IP: {ip_address}
📌 Местоположение: {location}
🖥️ Устройство: {user_agent}
    """

    return message
