import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

try:
    conn = psycopg2.connect(os.getenv("DB_URI"))
    print("Database connection successful!")
    conn.close()
except Exception as e:
    print(f"Database connection failed: {e}")