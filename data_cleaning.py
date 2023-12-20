import pandas as pd

class DataCleaning:
    
    
    def clean_card_data(self, df):
        # Implement your data cleaning logic for card data here
        # Remove erroneous values, NULL values, or errors with formatting

        # Placeholder: Drop rows with any NULL values
        cleaned_df = df.dropna()

        return cleaned_df 

    
    def called_clean_store_data(self, store_data):  
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
            # Implement your logic to convert weight to kg
            # Use a 1:1 ration of ml to g as a rough estimate for ml rows

            # Example: Convert 'weight' column to float
            products_df['weight'] = products_df['weight'].apply(lambda x: DataCleaning.convert_to_kg(x))
            return products_df

        except Exception as e:
            print(f"Error converting product weights: {e}")
            return None 

    def convert_to_kg(self, weight):
        # Implement your logic to convert different units to kg
        # Example: 1 g = 0.001 kg, 1 ml = 0.001 kg
        return float(weight) * 0.001 if 'g' in str(weight) else float(weight)

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
