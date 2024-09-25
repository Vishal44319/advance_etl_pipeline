import requests
import pandas as pd
from sqlalchemy import create_engine

# Function to fetch weather data from the OpenWeather API
def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None

# Function to transform the weather data into a Pandas DataFrame
def transform_weather_data(raw_data):
    if raw_data:
        weather_info = {
            'city': raw_data['name'],
            'temperature': raw_data['main']['temp'],
            'humidity': raw_data['main']['humidity'],
            'pressure': raw_data['main']['pressure'],
            'weather': raw_data['weather'][0]['description']
        }
        return pd.DataFrame([weather_info])
    else:
        print("No data to transform")
        return None

# Function to load the transformed data into a PostgreSQL database
def load_data_to_db(data, db_url):
    engine = create_engine(db_url)
    
    try:
        data.to_sql('weather_data', engine, if_exists='append', index=False)
        print("Data successfully loaded into the database")
    except Exception as e:
        print(f"Error loading data to the database: {e}")

# Main ETL function to extract, transform, and load data
def main():
    api_key = '4c7f980893c1d3c5776516619348eee3'  # Replace with your actual API key
    db_url = 'postgresql://postgres:Jaimatadi%402024@localhost:5433/etl_project_db' # Replace with your actual DB credentials
    cities = ['New York', 'Los Angeles', 'Chicago']

    all_weather_data = pd.DataFrame()

    for city in cities:
        # Step 1: Extract data
        raw_data = fetch_weather_data(city, api_key)
        
        # Step 2: Transform data
        transformed_data = transform_weather_data(raw_data)
        
        if transformed_data is not None:
            all_weather_data = pd.concat([all_weather_data, transformed_data], ignore_index=True)

    # Step 3: Load data into database
    if not all_weather_data.empty:
        load_data_to_db(all_weather_data, db_url)
    else:
        print("No data to load")

if __name__ == "__main__":
    main()