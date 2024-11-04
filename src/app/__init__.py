from flask import Flask
from app.controllers.book_controller import book_blueprint
from app.controllers.user_controller import user_blueprint
from app.utils.config import load_config
from app.utils.logger import configure_logging

# Function to create and configure the Flask app

def create_app():
    # Initialize the Flask application
    app = Flask(__name__)

    # Load configuration
    config = load_config()
    app.config.from_object(config)

    # Configure logging
    configure_logging()

    # Register blueprints
    app.register_blueprint(book_blueprint, url_prefix='/api/books')
    app.register_blueprint(user_blueprint, url_prefix='/api/users')

    # Return the configured Flask app
    return app
