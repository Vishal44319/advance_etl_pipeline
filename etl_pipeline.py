import requests
import pandas as pd
import sqlite3

# 1. Extract Phase: Extract data from OpenWeather API
def extract_weather_data(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # return the data as a dictionary
    else:
        print("Error fetching data from API")
        return None

# 2. Transform Phase: Clean and transform the data
def transform_weather_data(data):
    if data:
        main_data = data['main']
        weather_info = {
            'city': data['name'],
            'temperature_Celsius': main_data['temp'] - 273.15,  # Convert from Kelvin to Celsius
            'pressure': main_data['pressure'],
            'humidity': main_data['humidity'],
            'weather': data['weather'][0]['description']
        }

        # Create a DataFrame for easier manipulation
        df = pd.DataFrame([weather_info])
        return df
    else:
        print("No data to transform")
        return None

# 3. Load Phase: Load the transformed data into an SQLite database
def load_data_to_db(df, db_name='weather_data.db'):
    try:
        # Connect to SQLite database (or create it)
        conn = sqlite3.connect(db_name)
        
        # Load the data into a table called 'weather'
        df.to_sql('weather', conn, if_exists='append', index=False)
        print("Data successfully loaded into the database")
    except Exception as e:
        print(f"Error loading data into database: {e}")
    finally:
        conn.close()

# 4. ETL Execution: Combine the steps into a single function
def run_etl(api_key, city):
    # Step 1: Extract
    raw_data = extract_weather_data(api_key, city)
    
    # Step 2: Transform
    transformed_data = transform_weather_data(raw_data)
    
    # Step 3: Load
    if transformed_data is not None:
        load_data_to_db(transformed_data)
    else:
        print("No data to load")

if __name__ == "__main__":
    # Replace with your OpenWeather API key
    api_key = '4c7f980893c1d3c5776516619348eee3'
    
    # Specify the city for which you want the weather data
    city = 'New York'
    
    # Run the ETL pipeline
    run_etl(api_key, city)
