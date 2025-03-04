from flask import Flask
from flask_migrate import Migrate
from app.database import db
from app.routes import bp as api_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    migrate = Migrate(app, db)
    
    app.register_blueprint(api_blueprint)

    return app
