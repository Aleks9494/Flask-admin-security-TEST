import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test_admin.db') # БД ORM
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
SECRET_KEY = 'any long long long long long key'

# Flask-Security config
SECURITY_URL_PREFIX = "/admin"
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"

SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_REGISTER_URL = "/register/"
SECURITY_CHANGE_URL = "/change/"
SECURITY_RESET_URL = "/reset/"

SECURITY_POST_LOGIN_VIEW = "/admin/"
SECURITY_POST_LOGOUT_VIEW = "/admin/"
SECURITY_POST_REGISTER_VIEW = "/admin/"
SECURITY_POST_CHANGE_VIEW = "/admin/"

# Flask-Security features
SECURITY_REGISTERABLE = True #для регистрации
SECURITY_CHANGEABLE = True #для смены пароля
SECURITY_RECOVERABLE = True #сброс пароля
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
SECURITY_SEND_PASSWORD_RESET_EMAIL = True #отправка почты с инструкциями для смены смены пароля
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECURITY_LOGIN_USER_TEMPLATE = 'security/login_user.html'
SECURITY_REGISTER_USER_TEMPLATE = 'security/register_user.html'
SECURITY_CHANGE_PASSWORD_TEMPLATE = 'security/change_password.html'#представление для смены пароля
SECURITY_RESET_PASSWORD_TEMPLATE = 'security/reset_password.html' #представление, если нажали забыть пароль, перешли сюда для его смены
SECURITY_FORGOT_PASSWORD_TEMPLATE = 'security/forgot_password.html' #представление, если нажали забыть пароль, отправка на мейл действий для смены пароля

"""Сброс и восстановление пароля доступны, когда пользователь забывает свой пароль. 
Flask-Security отправляет пользователю электронное письмо со ссылкой на представление, в котором 
он может сбросить свой пароль. После сброса пароля они автоматически входят в систему и 
могут использовать новый пароль с этого момента. 
Ссылки для сброса пароля могут быть настроены на истечение срока действия через определенное время.
Т.Е. forgot_password и reset_password должны выполняться вместе + flask-mail для отправки инструкций на почту"""

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'testmail@gmail.com'  # введите свой адрес электронной почты здесь
MAIL_DEFAULT_SENDER = 'testmail@gmail.com'  # и здесь
MAIL_PASSWORD = 'Password'  # введите пароль






