import yaml
from sqlalchemy import create_engine

class DatabaseConncector:

    def read_db_creds():
        with open('db_creds.yaml','r') as file:
            db_creds = yaml.safe_load(file)
        return db_creds

    

        