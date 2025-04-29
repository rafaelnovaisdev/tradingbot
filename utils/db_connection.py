import yaml
import os
from sqlalchemy import create_engine

def load_db_config():
    config_path = os.path.join(os.path.dirname(__file__), '../config.yaml')
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config['database']

def get_db_engine():
    db_config = load_db_config()
    user = db_config['user']
    password = db_config['password']
    host = db_config['host']
    port = db_config['port']
    dbname = db_config['dbname']
    
    url = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
    engine = create_engine(url)
    return engine