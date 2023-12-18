import pandas as pd
import tabula

class DataExtractor:
    
    def read_rds_table(self,db_connector, table_name='dim_users'):
        query = f"SELECT * FROM {table_name}"
        data = pd.read_sql(query, db_connector.conn)
        return data

    def retrieve_pdf_data(self,pdf_link):
        # Method to extract data from a PDF using tabula-py
        try:
            # Use tabula to extract tables from the PDF
            tables= tabula.read_pdf(pdf_link, page='all', multiple_tables=True)

            # Combine tables into a single DataFrame
            df= pd.concat(tables, ignore_index=True)

            return df

        except Exception as e:
            print(f"Error extracting data from PDF: {e}")
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