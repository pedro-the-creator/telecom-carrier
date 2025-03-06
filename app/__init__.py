from flask import Flask
from flask_migrate import Migrate
from app.database import db
from app.routes import bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    Migrate(app, db)
    
    app.register_blueprint(bp)

    return app
