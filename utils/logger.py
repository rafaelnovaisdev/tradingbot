import logging
import os

def setup_logger(name, log_file='app.log', level=logging.INFO):
    log_path = os.path.join(os.path.dirname(__file__), '../logs')
    os.makedirs(log_path, exist_ok=True)

    log_file = os.path.join(log_path, log_file)

    handler = logging.FileHandler(log_file)        
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger