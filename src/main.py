from flask import Flask
from app.controllers.book_controller import book_blueprint
from app.controllers.user_controller import user_blueprint
from app.utils.config import load_config
from app.utils.logger import configure_logging

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

@app.route('/')
def index():
    return "Welcome to the Book Recommender Hub API"

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)