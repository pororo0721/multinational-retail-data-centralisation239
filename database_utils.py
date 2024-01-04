import yaml
from sqlalchemy import create_engine, inspect
from sqlalchemy import text



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

    def change_data_types(self, table_name, column_types):
        try:
            if not self.conn or self.conn.closed:
                print("Database connection is not established.")
                return   

            for column, new_type in column_types.items():
                # Generate SQL query to alter column data type
                query = text(f"ALTER TABLE {table_name} ALTER COLUMN {column} TYPE {new_type};")

                # Execute the query
                self.conn.execute(query)

            print(f"Data types for columns in {table_name} updated successfully.")
        except Exception as e:
            print(f"Error changing data types: {e}") 

    def update_legacy_store_details(self):
        try:
            if not self.conn or self.conn.closed:
                print("Database connection is not established.")
                return

            # SQL statement to merge latitude columns
            merge_latitude_sql = "UPDATE legacy_store_details SET latitude = COALESCE(lat, latitude);"
            self.execute_sql_query(merge_latitude_sql)    

        # SQL statements for updating legacy_store_details
            sql_statements = [
                "ALTER TABLE legacy_store_details ALTER COLUMN longitude TYPE FLOAT USING longitude::FLOAT;",
                "ALTER TABLE legacy_store_details ALTER COLUMN locality TYPE VARCHAR(255);",
                "ALTER TABLE legacy_store_details ALTER COLUMN store_code TYPE VARCHAR(255);",
                "ALTER TABLE legacy_store_details ALTER COLUMN staff_numbers TYPE SMALLINT;",
                "ALTER TABLE legacy_store_details ALTER COLUMN opening_date TYPE DATE;",
                "ALTER TABLE legacy_store_details ALTER COLUMN store_type TYPE VARCHAR(255) NULL;",
                "ALTER TABLE legacy_store_details ALTER COLUMN latitude TYPE FLOAT USING latitude::FLOAT;",
                "ALTER TABLE legacy_store_details ALTER COLUMN country_code TYPE VARCHAR(?);",  # Replace '?' with desired length
                "ALTER TABLE legacy_store_details ALTER COLUMN continent TYPE VARCHAR(255);",
                "UPDATE legacy_store_details SET location = 'N/A' WHERE location IS NULL;"
            ]

            # Execute the SQL statements
            for sql_statement in sql_statements:
                self.execute_sql_query(sql_statement)

            print("legacy_store_details updated successfully.")

        except Exception as e:
            print(f"Error updating legacy_store_details: {e}")
      
    def execute_sql_query(self, query):
        try:
            if not self.conn or self.conn.closed:
                print("Database connection is not established.")
                return

            # Convert the query string to a SQL text object
            sql_query = text(query)

            # Execute the query
            self.conn.execute(sql_query)

            print("SQL query executed successfully.")

        except Exception as e:
            print(f"Error executing SQL query: {e}")     


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

    def update_products_table(self):
        try:
            update_product_price_sql ="UPDATE dim_products SET product_price = REPLACE(product_price, '£','')::FLOAT;"
            self.execute_sql_query(update_product_price_sql)

            add_weight_class_sql= """
                ALTER TABLE dim_products
                ADD COLUMN weight_class VARCHAR(255);
            """

            self.execute_sql_query(add_weight_class_sql)

            update_weight_class_sql = """
                UPDATE dim_products
                SET weight_class =
                    CASE
                        WHEN weight <2 THEN 'Light'
                        WHEN weight >= 2 AND weight < 40 THEN  'Mid_Sized'
                        WHEN weight >= 40 AND weight <140 THEN 'Heavy'
                        WHEN weight >= 140 THEN 'Truck_Required'
                        ELSE 'Unknown'
                END;
            """
            self.execute_sql_query(update_weight_class_sql)

            print("Products table updated sucessfully.")

        except Exception as e:
            print(f"Error updating products table: {e}")                   
