from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        # Delay the import to avoid circular dependency
        from routes import register_blueprints
        register_blueprints(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
