from flask import Flask
from .models import db
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Register Blueprints
    from .routes.author_routes import author_bp
    from .routes.genre_routes import genre_bp
    from .routes.book_routes import book_bp

    app.register_blueprint(author_bp)
    app.register_blueprint(genre_bp)
    app.register_blueprint(book_bp)

    return app