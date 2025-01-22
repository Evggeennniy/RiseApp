import requests


def __get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?lang=en")
        data = response.json()
        if data["status"] == "success":
            return f"{data['country']} 🇦🇷, {data['regionName']} 📍, {data['city']} 🌆"
        else:
            return "Error in determining the location 🌍"
    except Exception:
        return "Error in determining the location 🚨"


def __get_client_ip(request):
    ip = request.headers.get('X-Forwarded-For', request.headers.get('X-Real-IP', request.remote_addr))

    if ip and "," in ip:
        ip = ip.split(",")[0].strip()

    return ip


def __get_information(request):
    ip_address = __get_client_ip(request)
    location = __get_ip_info(ip_address)
    user_agent = request.headers.get('User-Agent', 'Anonimous 🤷‍♂️')

    message = f"""
📊 Information about the request:
🌍 IP: {ip_address}
📌 Location: {location}
🖥️ Device: {user_agent}
    """

    return message
