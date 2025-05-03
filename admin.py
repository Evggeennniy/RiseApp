from flask import redirect
from models import db, User, MarketingLink
from flask_login import current_user
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated or not current_user.is_admin:
            return redirect('/login')
        return super().index()


class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


class SecureUserModelView(SecureModelView):
    column_list = ('id', 'username', 'is_admin')
    column_filters = ()
    column_searchable_list = ('id', 'username')
    column_labels = {
        'id': 'Идентификатор',
        'username': 'Имя пользователя',
        'password': 'Пароль',
        'is_admin': 'Админ'
    }


class SecureMarketingModelView(SecureModelView):
    column_list = ('id', 'title', 'visits')
    column_filters = ()
    column_searchable_list = ('id', 'title')
    column_labels = {
        'id': 'Идентификатор',
        'title': 'Заголовок',
        'link': 'Ссылка',
        'visits': 'Переходы'
    }

    form_widget_args = {
        'link': {
            'readonly': True
        },
        'visits': {
            'readonly': True
        },
    }

    def on_model_change(self, form, model, is_created):
        if is_created:
            db.session.flush()
            website_url = 'https://rise-app.software'
            model.link = f'{website_url}/?origin={model.id}'


def init_admin_panel(admin, db):
    admin.add_view(SecureUserModelView(User, db.session, 'Пользователи'))
    admin.add_view(SecureMarketingModelView(MarketingLink, db.session, 'Маркетинг'))
