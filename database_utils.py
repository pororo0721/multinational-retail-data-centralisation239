import yaml
from sqlalchemy import create_engine

class DatabaseConnector:

    def read_db_creds():
        with open('db_creds.yaml','r') as file:
            db_creds = yaml.safe_load(file)
        return db_creds

    
    def init_db_engine(self):
        db_creds=self.read_db_creds()
        engine= create_engine(f"postgresql://{db_creds['RDS_USER']}:{db_creds['RDS_PASSWORD']}@{db_creds['RDS_HOST']}:{db_creds['RDS_PORT']}/{db_creds['RDS_DATABASE']}")
        return engine

    def list_db_tables(self):
        engine = self.init_db_engine()
        tables = engine.tables_names()
        return tables

    def upload_to_db(self, df, tables_names):
        # Implement logic to upload DataFrame to the specified database table
        pass        