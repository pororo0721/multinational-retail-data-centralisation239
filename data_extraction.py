import pandas as pd
import tabula
import requests
import boto3
from io import StringIO
from urllib.parse import urlsplit

class DataExtractor:
    
    def read_rds_table(self,db_connector, table_name='dim_users'):
        query = f"SELECT * FROM {table_name}"
        data = pd.read_sql(query, db_connector.conn)
        return data

    def retrieve_pdf_data(self, pdf_link):
    # Method to extract data from a PDF using tabula-py
        try:
        # Use tabula to extract tables from the PDF
            tables = tabula.read_pdf(pdf_link, pages='all', multiple_tables=True)

        # Check if tables were successfully extracted
            if tables:
            # Combine tables into a single DataFrame
                df = pd.concat(tables, ignore_index=True)
                return df
            else:
                print("No tables found in the PDF")
                return None

        except Exception as e:
            print(f"Error extracting data from PDF: {e}")
            return None

    def list_number_of_stores(self, number_stores_endpoint, headers):
        try:
            response = requests.get(number_stores_endpoint, headers=headers)
            if response.status_code== 200:
                return response.json().get('count')
            else:
                print(f"Failed to retrieve the number of stores. Status code: {response.status_code} ")
                return None 
        except Exception as e:
            print(f"Error retrieving the number of stores:{e}")
            return None  

    def retrieve_stores_data(self, store_endpoint, headers):
        try:
            response = requests.get(store_endpoint, headers=headers)
            if response.status_code == 200:
                stores_data = response.json().get('stores')
                if stores_data:
                    df= pd.DataFrame(stores_data)
                    return df
                else:
                    print("No store data foun in the API response.")
                    return None
            else:
                print(f"Failed to retrieve store data. Status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error retrieveing store data : {e}")
            return None                                     


    @staticmethod
    def extract_csv(file_path):
        # Method to extract data from CSV file
        pass

    @staticmethod
    def extract_api(api_url):
        # Method to extract data from an API
        pass

    @staticmethod
    def extract_s3(s3_address):

        
        try:
            # Extract buckey_name and object_key from the S3 address
            url_parts = urlsplit(s3_address)
            if url_parts.scheme != 's3':
                raise ValueError("Invalid S3 address scheme. Expected 's3://'.")

            bucket_name= url_parts.netloc
            object_key= url_parts.path.lstrip('/')

            if not bucket_name or not object_key:
                raise ValueError("Invalid S3 address format. Expected 's3://<bucket_name>/<object_key>'.")
      
            # Extract data from S3 bucket
            s3_client= boto3.client('s3')
            response = s3_client.get_object(Bucket= bucket_name, key= object_key)
            data= response['Body'].read().decode('utf-8')

            # Create pandas DataFrame
            df=pd.read_csv(StringIO(data))
            return df

        except Exception as e:
            print(f"Error extracting data from s3: {e}")
            return None    
