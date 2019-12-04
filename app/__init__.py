from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.main import config
    app.config.from_object(config.Config)

    from app.main import db, login, crypt, mail
    db.init_app(app)
    login.init_app(app)
    login.login_view = 'main.login'
    crypt.init_app(app)
    mail.init_app(app)

    from app.main import bp
    app.register_blueprint(bp)

    return app
