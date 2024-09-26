from extract.extract_api import extract_api
from transform.clean_data import clean_data
from load.load_to_csv import load_to_csv

if __name__ == "__main__":
    # Step 1: Extract data from the API
    api_url = "https://jsonplaceholder.typicode.com/posts"
    df = extract_api(api_url)

    # Step 2: Clean and transform the data
    if df is not None:
        df_cleaned = clean_data(df)

        # Step 3: Load the cleaned data into a CSV file
        load_to_csv(df_cleaned, file_name="cleaned_data.csv")