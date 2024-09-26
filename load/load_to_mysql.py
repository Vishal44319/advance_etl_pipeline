from sqlalchemy import create_engine
import pandas as pd

def load_to_mysql(df, table_name, connection_string):
    """
    Load data into a MySQL database.

    Args:
    - df (pd.DataFrame): Cleaned data to be loaded.
    - table_name (str): Name of the table to load the data into.
    - connection_string (str): Connection string for the MySQL database.
    """
    try:
        # Create a SQLAlchemy engine
        engine = create_engine(connection_string)

        # Load the DataFrame into the database table
        df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

        print(f"Data loaded successfully into {table_name} table.")
    except Exception as e:
        print(f"Error loading data into MySQL: {e}") 
