from flask import Flask
from config import Config
from app.extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    # IMPORT BLUEPRINTS
    from app.routes.auth import auth
    from app.routes.main import main
    from app.routes.video import video

    # REGISTER
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(video)

    return app