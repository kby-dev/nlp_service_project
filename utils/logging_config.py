import logging
import sys
from pythonjsonlogger import jsonlogger
import os

def setup_logger(log_file: str = "logs/service.log"):
    """
    Configures structured logging for the app.
    Logs go both to stdout and a local file.
    """
    # Create logs folder if it doesn't exist
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # JSON formatter
    formatter = jsonlogger.JsonFormatter(
        '%(asctime)s %(name)s %(levelname)s %(message)s'
    )

    # Console logging
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File logging
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
