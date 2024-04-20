from flask import Flask
from config import Config
from app.extensions import db, migrate, jwt, login_manager

from app.tweet import tweetBp
from app.user import userBp
from app.auth import authBp
from app.frontend import frontendBp

from datetime import timedelta

# import models
from app.models.tweet import Tweets
from app.models.user import Users

# import flask admin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
# import custom model view
from app.admin.CustomModelView import CustomModelView, AdminModelView

from flask_login import current_user

def create_app(config_class=Config):
    # Konfigurasi APP
    app = Flask(__name__)
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
    app.config.from_object(config_class)

    # inisiasi admin panel
    admin = Admin(app, name="Dashboard", template_mode='bootstrap4', index_view=AdminModelView("home"), url='/')

    # Initilizae database & migration
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)

    admin.add_view(CustomModelView(Users, db.session))
    admin.add_view(CustomModelView(Tweets, db.session))

    # initilize blueprint
    app.register_blueprint(frontendBp, url_prefix='/')
    app.register_blueprint(tweetBp, url_prefix='/api/tweets')
    app.register_blueprint(userBp, url_prefix='/api/users')
    app.register_blueprint(authBp, url_prefix='/api/auth')

    return app