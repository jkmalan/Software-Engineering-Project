from os import environ, getenv, path

db_dir = path.join(path.dirname(path.abspath(__file__)), 'database')


class Config(object):
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or \
    'sqlite:///' + path.join(db_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = getenv('SECRET_KEY', 'my_precious_secret_key')

    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USERNAME = 'sentijournalapp@gmail.com'
    MAIL_PASSWORD = 'sentijournalapp'
    MAIL_USE_SSL=True

    # CHATBOT SETTINGS
    CHATBOT_DATABASE_URI = 'sqlite:///' + path.join(db_dir, 'bot.db')
