import uuid
import requests
from flask import request, render_template, url_for, redirect, abort, flash
from utils.request_tools import get_request_info
from flask_login import login_user
from utils.telegram_tools import send_telegram_message
from app import get_locale, move_group_id, bot_token, notify_group_id, recaptcha_secret_key, recaptcha_key
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from models import db, User, MarketingLink


def init_routers(app):
    @app.route('/')
    def index():
        origin_id = request.args.get("origin")
        if request.args.get("origin"):
            marked_link = MarketingLink.query.get(origin_id)
            marked_link.visits += 1
            db.session.commit()

        return render_template('index.html', lang=get_locale(), recaptcha_key=recaptcha_key)

    @app.route('/trendcity')
    def project_1():
        return render_template('trendcity.html', lang=get_locale())

    @app.route('/prolearn')
    def project_2():
        return render_template('prolearn.html', lang=get_locale())

    @app.route('/skillpoint')
    def project_3():
        return render_template('skillpoint.html', lang=get_locale())

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]

            if User.query.count() == 0:
                init_user = User(
                    username=username,
                    password=generate_password_hash(password),
                    is_admin=True
                )
                db.session.add(init_user)
                db.session.commit()

                flash("Инициализирован админ")
                return redirect(url_for("login"))

            user = User.query.filter_by(username=username).first()
            if user and check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("admin.index"))
            else:
                flash("Невірний логін або пароль")
                return redirect(url_for("login"))

        return render_template("login.html")

    @app.after_request
    def after_request_handler(response):
        if request.path.startswith('/static') \
                or request.path.startswith('/admin') \
                or request.path.startswith('/favicon.ico') \
                or request.path.startswith('/send-message'):
            return response

        request_uuid = request.cookies.get('uuid')
        if not request_uuid:
            request_uuid = uuid.uuid4()
            response.set_cookie('uuid', str(request_uuid))

        request_info = get_request_info(request)

        log = f"""
📊 Cought a move by:
-------------------------------
🔗 Link: {request.url}
🆔 ID: {request_uuid}
🌍 IP: {request_info.get('user_ip')}
📌 Location: {request_info.get('user_location')}
🖥️ Device: {request_info.get('user_agent')}
-------------------------------
    """

        send_telegram_message(move_group_id, log, bot_token)

        return response

    @app.route('/send-message', methods=['POST'])
    def send_message():
        if request.method != 'POST':
            return

        token = request.form.get("g-recaptcha-response")
        remote_ip = request.remote_addr

        payload = {
            "secret": recaptcha_secret_key,
            "response": token,
            "remoteip": remote_ip
        }

        r = requests.post("https://www.google.com/recaptcha/api/siteverify", data=payload)
        result = r.json()

        score = result.get("score", "0")
        if not result.get("success") or score < 0.5:
            return abort(404)

        request_info = get_request_info(request)

        log = f"""
🚀 Got a request by:
-------------------------------
👤 Name: {request.form.get('person_name', 'Undefined')}
📱 Phone: {request.form.get('person_phone', 'Undefined')}
📱 Email: {request.form.get('person_email', 'Undefined')}
💬 Message: {request.form.get('person_note', 'Undefined')}
-------------------------------
📊 About the request:
-------------------------------
🔗 Link: {request.url}
🆔 ID: {request.cookies.get('uuid')}
🌍 IP: {request_info.get('user_ip')}
📌 Location: {request_info.get('user_location')}
🖥️ Device: {request_info.get('user_agent')}
-------------------------------
👨🏻‍💻 RiseApp Team
    """
        send_telegram_message(notify_group_id, log, bot_token)
        return redirect(url_for('index'))
