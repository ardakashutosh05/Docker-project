from flask import Flask
import redis
import psycopg2
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379)

@app.route("/")
def home():
    try:
        r.incr("hits")
        hits = r.get("hits").decode()

        return f"🚀 Visits: {hits}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
