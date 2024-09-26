 import pandas as pd

def extract_csv(file_path):
    """
    Extract data from a CSV file.

    Args:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: DataFrame containing the CSV data.
    """
    try:
        # Load data from CSV
        data = pd.read_csv(file_path)
        print("Data extracted successfully from CSV.")
        return data
    except Exception as e:
        print(f"Error extracting CSV: {e}")
        return None