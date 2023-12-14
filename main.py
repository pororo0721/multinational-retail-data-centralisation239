# Example Usage
from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# Step 1
db_connector = DatabaseConnector()
db_connector.init_db_engine()

# Step 2
tables = db_connector.list_db_tables()
print("Available tables:", tables)

# Step 3
data_extractor = DataExtractor()
user_data = data_extractor.read_rds_table(db_connector)

# Step 4
data_cleaning = DataCleaning()
cleaned_user_data= data_cleaning.cleaned_user_data(user_data)

# Step 5
db_connector.upload_to_db(cleaned_user_data, 'dim_users')

# Step 6
db_connector.disconnect()

