from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# Step 1
db_creds= yaml.safe_load(open("db_creds.yaml"))

# Step 2
db_connector= DatabaseConnector(db_creds)

# Step 3
db_connector.connect()

# Step 4
tables = db_connector.list_db_tables()
print("Abailable tables:", tables)