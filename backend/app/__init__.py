from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.models import db
from app.routes import register_routes
from app.routes.prospect_routes import prospect_bp

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    register_routes(app)

    with app.app_context():
        from app import routes  

    return app


app = create_app() 
