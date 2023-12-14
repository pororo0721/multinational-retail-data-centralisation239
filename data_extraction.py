import pandas as pd

class DataExtractor:
    
    def read_rds_table(self,db_connector, table_name='dim_users'):
        query = f"SELECT * FROM {table_name}"
        data = pd.read_sql(query, db_connector.conn)
        return data

    @staticmethod
    def extract_csv(file_path):
        # Method to extract data from CSV file
        pass

    @staticmethod
    def extract_api(api_url):
        # Method to extract data from an API
        pass

    @staticmethod
    def extract_s3(bucket_name, object_key):
        # Method to extract data from an S3 bucket
        pass