import yaml
from sqlalchemy import create_engine, inspect

class DatabaseConnector:
    def __init__(self):
        self.conn = None

    def read_db_creds(self, file_path="db_creds.yaml"):
        with open(file_path, 'r') as file:
            db_creds = yaml.safe_load(file)
        return db_creds

    def init_db_engine(self):
        try:
            db_creds = self.read_db_creds()
            db_url = f"postgresql://{db_creds['RDS_USER']}:{db_creds['RDS_PASSWORD']}@{db_creds['RDS_HOST']}:{db_creds['RDS_PORT']}/{db_creds['RDS_DATABASE']}"
            print(f"Database URL: {db_url}")
            self.conn = create_engine(db_url).connect()
            print("Database connection established successfully.")
        except Exception as e:
            print(f"Error establishing database connection: {e}")    

    def list_db_tables(self):
        inspector = inspect(self.conn)
        tables = inspector.get_table_names()
        return tables

    def upload_to_db(self, data, table_name):
        data.to_sql(table_name, self.conn, if_exists='replace', index=False)

    def disconnect(self):
        if self.conn:
            self.conn.close()

# inherit from DatabaseConnector
class DatabaseUploader(DatabaseConnector):
    def upload_card_data(self, data, table_name):
        if not self.conn or not self.conn.closed:
            print("Database connection is not established.")
            return
        
        self.upload_to_db(data, table_name)            
