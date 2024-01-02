# Example Usage
from database_utils import DatabaseConnector, DatabaseUploader
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# Step 1
db_connector = DatabaseConnector()
db_connector.init_db_engine()

# Step 2
# tables = db_connector.list_db_tables()
# print("Available tables:", tables)

# Step 3
data_extractor = DataExtractor()
# user_data = data_extractor.read_rds_table(db_connector)

# # Step 4
data_cleaning = DataCleaning()
# cleaned_user_data= data_cleaning.cleaned_user_data(user_data)

# # Step 5
# db_connector.upload_to_db(cleaned_user_data, 'dim_users')

# # Step 6
# db_connector.disconnect()

# Task 4: Extracting users and cleaning card details

# Step 1,2: Extract card data from PDF
# pdf_link_card=r"C:\Users\Sinhye\Documents\GitHub\multinational-retail-data-centralisation239\card_details.pdf"
# card_data_extractor= DataExtractor()
# card_data= card_data_extractor.retrieve_pdf_data(pdf_link_card)

# Step 3: Clean the card data
# card_data_cleaning= DataCleaning()
# cleaned_card_data= card_data_cleaning.clean_card_data(card_data)

# Step 4: Upload cleaned card data to the database
db_uploader=DatabaseUploader()
# db_uploader.upload_card_data(cleaned_card_data, 'dim_card_details')

# Task 5: Extract and clean the details of each store

# Step 1,2: Retrieve the number of stores from the API
# number_stores_endpoint=" https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
# headers={'x-api-key' : 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
# list_number_of_stores= data_extractor.list_number_of_stores(number_stores_endpoint,headers)

# Step 3: Retrieve store data from the API
# store_endpoint="https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}"
# store_data= data_extractor.retrieve_stores_data(store_endpoint, headers)

# Step 4: Clean the store data
# store_data_cleaning = DataCleaning()
# cleaned_store_data = store_data_cleaning.called_clean_store_data(store_data)

# Step 5: Upload cleaned store data to the database
# db_uploader=DatabaseUploader()

# if cleaned_store_data is not None:
#     db_uploader.upload_to_db(cleaned_store_data, 'dim_store_details')
# else:
#     print("Error: cleaned_store_data is None. Upload to the database skipped.")  
#

# Task 6: Extract and clean the product details

# Step 1 : 
# products_df = data_extractor.extract_s3('s3://data-handling-public/products.csv')

# Step 2:
# cleaned_products_df = data_cleaning.convert_product_weights(products_df)

# Step 3:
# cleaned_products_df= data_cleaning.clean_products_data(cleaned_products_df)

# Step 4:
# db_uploader.init_db_engine()

# if cleaned_products_df is not None: 
#     db_uploader.upload_to_db(cleaned_products_df, 'dim_products')
# else:
#     print("Error: Cleaned_products_df is None. Upload to the database skipped.")    

# Task 7: Retrieve and clean the orders table

# Step1: List all tables in the database
# tables = db_connector.list_db_tables()
# print("Available tables:", tables)

# Step 2: Extract orders data
# orderes_data= data_extractor.read_rds_table(db_connector, table_name='orders_table')

# Step 3: Clean orders data
# cleaned_orders_data= data_cleaning.clean_orders_data(orderes_data)

# Step 4: Upload cleaned data to the database
# db_uploader.init_db_engine()

# if cleaned_orders_data is not None:
#     db_uploader.upload_to_db(cleaned_orders_data, 'orders_table')
#     print("Orders data uploaded successfully.")
# else:
#     print("Errpr: Cleaned_orders_data is None. Upload to the database skipped.")    

# Task 8: Retrieve and clean the data events data.

#  Step 1: Extract JSON data
json_data = data_extractor.extract_json('s3://data-handling-public/date_details.json')
