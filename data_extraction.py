import pandas as pd
import tabula

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

    def list_number_of_stores(self, number_stores_endpoint, header):
        try:
            response = requests.get(number_stores_endpoint, header=header)
            if response.status_code== 200:
                return response.json().get('count')
            else:
                print(f"Failed to retrieve the number of stores. Status code: {response.status_code} ")
                return None 
        except Exception as e:
            print(f"Error retrieving the number of stores:{e}")
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
    def extract_s3(bucket_name, object_key):
        # Method to extract data from an S3 bucket
        pass