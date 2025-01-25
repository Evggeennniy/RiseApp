import requests


def __get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?lang=en")
        data = response.json()
        if data["status"] == "success":
            return f"{data['country']} 🏁, region {data['regionName']} 📍, city {data['city']} 🌆"
        else:
            return "Error in determining the location 🌍"
    except Exception:
        return "Error in determining the location 🚨"


def __get_client_ip(request):
    ip = request.headers.get('X-Forwarded-For', request.headers.get('X-Real-IP', request.remote_addr))

    if ip and "," in ip:
        ip = ip.split(",")[0].strip()

    return ip


def __get_user_agent(headers):
    return headers.get('User-Agent', 'Anonimous 🤷‍♂️')


def get_request_info(request) -> dict:
    """
    Returns a dict with data about the request
    """

    user_ip = __get_client_ip(request)
    user_location = __get_ip_info(user_ip)
    user_agent = __get_user_agent(request.headers)

    return {
        'user_ip': user_ip,
        'user_location': user_location,
        'user_agent': user_agent
    }
