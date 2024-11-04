import logging

# Function to configure logging for the application

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )

    # Set up logging for specific libraries if needed
    logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

    # Example of logging a startup message
    logger = logging.getLogger(__name__)
    logger.info("Logging configured successfully.")