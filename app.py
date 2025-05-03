import os
from dotenv import load_dotenv
from flask import Flask, request
from flask_babel import Babel, _

from flask_migrate import Migrate
from flask_admin import Admin
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

from admin import MyAdminIndexView
from models import User


def get_locale():
    lang = request.args.get('lang')
    if not lang:
        lang = request.accept_languages.best_match(['uk', 'ru', 'en'])

    return lang or 'en'


load_dotenv()

bot_token = os.getenv("TG_BOT_TOKEN")
move_group_id = os.getenv("TG_MOVE_GROUP_ID")
notify_group_id = os.getenv("TG_NOTIFY_GROUP_ID")
recaptcha_key = os.getenv("RECAPTCHA_SITE_KEY")
recaptcha_secret_key = os.getenv("RECAPTCHA_SITE_KEY")


def setup(app=Flask(__name__)):
    from routes import init_routers
    from admin import init_admin_panel
    from models import db

    admin = Admin(app, name='Адмін-панель', template_mode='bootstrap4', index_view=MyAdminIndexView())
    login_manager = LoginManager(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.secret_key = os.getenv("SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

    Babel().init_app(app, locale_selector=get_locale)
    CSRFProtect(app)
    db.init_app(app)
    Migrate(app, db)
    init_routers(app)
    init_admin_panel(admin, db)

    with app.app_context():
        db.create_all()

    return app
