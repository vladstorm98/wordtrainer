from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from myapp.api import api as api_blueprint  # noqa
    app.register_blueprint(api_blueprint)

    return app

from myapp.models.dictionaries import Dictionaries  # noqa
from myapp.models.words import Words  # noqa
from myapp import api  # noqa
