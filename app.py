import psycopg2
import os

db_host = os.getenv("DB_HOST", "db")

conn = psycopg2.connect(
    host=db_host,
    database="mydb",
    user="admin",
    password="admin"
)

print("✅ Connected to DB")
