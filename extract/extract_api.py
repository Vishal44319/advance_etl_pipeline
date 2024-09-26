 
import requests
import pandas as pd

def extract_api(api_url):
    """
    Extract data from an API.

    Args:
    - api_url (str): URL of the API endpoint.

    Returns:
    - pd.DataFrame: DataFrame containing the API data.
    """
    try:
        # Make a GET request to the API
        response = requests.get(api_url)
        
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # Convert JSON response to DataFrame
        data = response.json()
        df = pd.DataFrame(data)
        
        print("Data extracted successfully from API.")
        return df
    except requests.exceptions.RequestException as e:
        print(f"Error extracting API data: {e}")
        return None