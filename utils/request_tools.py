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


FORBIDDEN_LOCATIONS = {
    'United Kingdom',
    'United States',
    'Russia'
}
FORBIDDEN_HEADERS = [
    "bot",
    "crawl",
    "spider",
    "scrape",
    "scanner",
    "checker",
    "fetch",
    "parser",
    "monitor",
    "watcher",
    "listener",
    "agent",
    "ai",
    "assistant",
    "automa",
    "notifier",
    "dispatcher",
    "client",
    "python",
    "curl",
    "requests",
    "axios",
    "http",
    "headless",
    "node-fetch",
    "go-http",
    "wget",
    "libwww",
    "Postman",
    "Java/",
    "Java-Client",
    "httpclient",
    "urlgrabber",
    "HttpClient",
    "fetcher",
    "phantomjs",
    "selenium",
    "scrapy",
    "mechanize"
]


def is_allowed_to_action(req_data):
    user_location = req_data.get('user_location').lower()
    user_agent = req_data.get('user_agent').lower()

    for header in FORBIDDEN_HEADERS:
        if header in user_agent:
            return False

    for location in FORBIDDEN_LOCATIONS:
        if location in user_location:
            return False

    return True
