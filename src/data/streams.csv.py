import duckdb 
import pandas as pd 
from dotenv import load_dotenv
import os 
import sys 

load_dotenv()

def initialise_connection():
    """Initialise a connection to the database."""
    if not os.environ.get("MOTHERDUCK_TOKEN"):
        raise ValueError("MotherDuck token not found")
    conn = duckdb.connect(database='md:')
    try:
        conn.execute(f"USE {os.environ.get('DATABASE_NAME')}")
    except duckdb.Error as e:
        raise RuntimeError(f"Failed to initialise MotherDuck database connection: {e}")
    return conn

def fetch_data_from_db():
    """Fetch all data from the table channel_stats as this can efficiently be processed client side with DuckDB wasm."""
    conn = initialise_connection()
    cursor = conn.execute("SELECT * FROM channel_stats")
    data = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    df = pd.DataFrame(data, columns=column_names)
    return df 



df = fetch_data_from_db()
df.to_csv(sys.stdout, index=False)




