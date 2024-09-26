import pandas as pd

def load_to_csv(df, file_name):
    """
    Load data into a CSV file.

    Args:
    - df (pd.DataFrame): Cleaned data to be loaded.
    - file_name (str): Name of the CSV file to save the data to.
    """
    try:
        df.to_csv(file_name, index=False)
        print(f"Data loaded successfully into {file_name}.")
    except Exception as e:
        print(f"Error loading data into CSV: {e}")