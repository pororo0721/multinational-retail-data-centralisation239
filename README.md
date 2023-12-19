# multinational-retail-data-centralisation239

## _Milestone 2: Extract and clean the data from the data sources_

### Task 1: Set up a new database to store the data

- Initialise a new database locally to store the extracted data.
- Set up a new database within pgAdmin4 and name it sales_data.

### Task 2: Initialise the three project classes
In this task, define scripts and classes for extracting and cleaning data from various sources. Class methods will be defined as needed in subsequent tasks.

Step 1: Create a new Python script named data_extraction.py and within it, create a class named DataExtractor.
This class will work as a utility class, in it you will be creating methods that help extract data from different data sources.
The methods contained will be fit to extract data from a particular data source, these sources will include CSV files, an API and an S3 bucket.

Step 2: Create another script named database_utils.py and within it, create a class DatabaseConnector which you will use to connect with and upload data to the database.
Step 3: Finally, create a script named data_cleaning.py this script will contain a class DataCleaning with methods to clean data from each of the data sources.

### Task 3: Extract and clean the user data
The historical data of users is stored in an AWS database in the cloud. Develop methods to extract and clean this information.

Step 1: Create a db_creds.yaml file containing the database credentials.

Step 2: Implement methods in your DatabaseConnector class:

- read_db_creds: Reads the credentials from the YAML file.
- init_db_engine: Initializes and returns an SQLAlchemy database engine.
- list_db_tables: Lists all tables in the database.

Step 4: Develop a method in your DataExtractor class:

- read_rds_table: Extracts a specified database table to a Pandas DataFrame.

Step 6: Create a method in your DataCleaning class:

- clean_user_data: Cleans user data, handling NULL values, date errors, type errors, and incorrect information.

Step 8:  Upload the cleaned user data to the dim_users table in the sales_data database using the upload_to_db method.

### Task 4: Extracting users and cleaning card details

The users' card details are stored in a PDF document in an AWS S3 bucket.

Step 1: Install the tabula-py Python package for extracting data from PDF documents.

Step 2: Implement a method in your DataExtractor class:

- retrieve_pdf_data: Extracts data from a given PDF link using tabula-py and returns a Pandas DataFrame.

Step 3: Create a method in your DataCleaning class:

- clean_card_data: Cleans card data, removing erroneous values, NULL values, and formatting errors.

Step 4: Upload the cleaned card details to the dim_card_details table in the sales_data database using the upload_to_db method.

### Task 5: Extract and clean the details of each store

Store data can be retrieved through an API with two GET methods.

Step 1: Implement a method in your DataExtractor class:

- list_number_of_stores: Returns the number of stores to extract. Takes the number of stores endpoint and header dictionary as arguments.

Step 3: Create another method:

- retrieve_stores_data: Takes the retrieve a store endpoint as an argument and extracts all the stores from the API, saving them in a Pandas DataFrame.

Step 4: Implement a method in the DataCleaning class:

- clean_store_data: Cleans the data retrieved from the API and returns a Pandas DataFrame.

Step 5: Upload the DataFrame to the sales_data database using the upload_to_db method, storing it in the dim_store_details table.
