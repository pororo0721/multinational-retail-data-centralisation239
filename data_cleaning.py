import pandas as pd

class DataCleaning:
    
    @staticmethod
    def clean_card_data(df):
        # Implement your data cleaning logic for card data here
        # Remove erroneous values, NULL values, or errors with formatting

        # Placeholder: Drop rows with any NULL values
        cleaned_df = df.dropna()

        return cleaned_df 

    @staticmethod
    def called_clean_store_data(store_data):  
        # This could include handling missing values, remobing duplicates, etc.
        try:
            if store_data is not None:
                cleaned_store_data = store_data.dropna()
                return cleaned_store_data

            else:
                print("Error: Store data is None.")
                return None
        except Exception as e:
            print(f"Error cleaning store data: {e}")
            return None
    
    @staticmethod
    def convert_product_weights(products_df):              
        try:
            # Assuming 'weight' column contains weights in different units
            # Implement logic to convert weight to kg
            # Use a 1:1 ration of ml to g as a rough estimate for ml rows

            # Example: Convert 'weight' column to float
            products_df['weight'] = products_df['weight'].apply(lambda x: DataCleaning.convert_to_kg(x))
            return products_df

        except Exception as e:
            print(f"Error converting product weights: {e}")
            return None 

    @staticmethod
    def convert_to_kg(weight):
        
        try:
            # If weight is not a string, return None
            if not isinstance(weight, str):
                return None

            # Remove non-numeric characters from the weight
            numeric_part= ''.join(filter(str.isdigit, weight)) 

            #  If the resulting string is empty, return None
            if not numeric_part:
                return None

            # Assuming 'g' is the default unit, convert to kg
            return float(numeric_part) * 0.001

        except Exception as e:
            print(f"Error converting weight to kg: {e}")
            return None  

    @staticmethod
    def clean_products_data(products_df):
        try:
            # Implement logic to clean the DataFrame of any additional erroneous values
            # Example: Drop rows with missing values
            cleaned_df = products_df.dropna()

            return cleaned_df

        except Exception as e:
            print(f"Error cleaning products data: {e}")
            return None

    @staticmethod
    def clean_orders_data(df):
        # Method to clean orders data
        try:
            #Remove unwated columns
            columns_to_remove =['first_name','last_name','1']
            cleaned_orders_data= df.drop(columns=columns_to_remove, errors='ignore')
            return cleaned_orders_data

        except Exception as e:
            print(f"Error cleaning orders data: {e}")
            return None      
        
    @staticmethod
    def clean_csv(data):
        # Method to clean data extracted from CSV   
        pass

    @staticmethod
    def clean_api_data(data):
        # Method to clean data extracted from an API
        pass

    @staticmethod
    def clean_s3_data(data):
        # Method to clean data extracted from an S3 bucket  
        pass

    @staticmethod
    def clean_user_data(data):
        # Implement your data cleaning logic here
        return data

