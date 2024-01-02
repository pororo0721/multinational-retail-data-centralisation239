import yaml
from sqlalchemy import create_engine, inspect

class DatabaseConnector:
    def __init__(self):
        self.conn = None 

    def init_db_engine(self):
        try:
            db_creds = self.read_db_creds()
            db_url = f"postgresql://{db_creds['RDS_USER']}:{db_creds['RDS_PASSWORD']}@{db_creds['RDS_HOST']}:{db_creds['RDS_PORT']}/{db_creds['RDS_DATABASE']}"
            print(f"Database URL: {db_url}")

            # Create a new engine with autocommit set to True
            engine = create_engine(
                db_url,
                isolation_level="AUTOCOMMIT",
                pool_pre_ping=True,
                connect_args={'sslmode': 'require'}
            )            
            self.conn = engine.connect()

            print("Database connection established successfully.")
        except Exception as e:
            print(f"Error establishing database connection: {e}")    

    def list_db_tables(self):
        inspector = inspect(self.conn)
        tables = inspector.get_table_names()
        return tables

    def upload_to_db(self, data, table_name):
        if self.conn is not None:
            data.to_sql(table_name, self.conn, if_exists='append', index=False)
        else:
            print("Database connection is None. Data upload skipped.")    
        

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print("Disconnected from the database.")
            # Reconnect after disconnection
            self.init_db_engine()

    def read_db_creds(self, file_path="db_creds.yaml"):
        with open(file_path, 'r') as file:
            db_creds = yaml.safe_load(file)
        return db_creds 

               

# inherit from DatabaseConnector
class DatabaseUploader(DatabaseConnector):
    def upload_card_data(self, data, table_name):
        try:
            self.init_db_engine()
            if not self.conn or not self.conn.closed:
                print("Database connection is not established.")
                return

            print(f"Uploading data to {table_name} table.")
            self.upload_to_db(data, table_name)
            print("Data upload successful.")
        except Exception as e:
            print(f"Error uploading data to the database: {e}")      
        finally:
            self.disconnect()
            print("Disconnected from the database.")              
