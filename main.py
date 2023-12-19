# Example Usage
from database_utils import DatabaseConnector, DatabaseUploader
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
# user_data = data_extractor.read_rds_table(db_connector)

# # Step 4
# data_cleaning = DataCleaning()
# cleaned_user_data= data_cleaning.cleaned_user_data(user_data)

# # Step 5
# db_connector.upload_to_db(cleaned_user_data, 'dim_users')

# # Step 6
# db_connector.disconnect()

# Step 7: Extract card data from PDF
pdf_link_card=r"C:\Users\Sinhye\Documents\GitHub\multinational-retail-data-centralisation239\card_details.pdf"
card_data_extractor= DataExtractor()
card_data= card_data_extractor.retrieve_pdf_data(pdf_link_card)

# Step 8: Clean the card data
card_data_cleaning= DataCleaning()
cleaned_card_data= card_data_cleaning.clean_card_data(card_data)

# Step 9: Upload cleaned card data to the database
db_uploader=DatabaseUploader()
db_uploader.upload_card_data(cleaned_card_data, 'dim_card_details')

# Step 10: Retrieve the number of stores from the API
number_stores_endpoint=" https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
headers={'x-api-key' : 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
list_number_of_stores= data_extractor.list_number_of_stores(number_stores_endpoint,headers)