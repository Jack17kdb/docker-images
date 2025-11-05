from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        database=os.environ.get("DB_NAME", "testdb"),
        user=os.environ.get("DB_USER", "testuser"),
        password=os.environ.get("DB_PASSWORD", "testpass")
    )

@app.route('/')
def home():
    return jsonify({"message": "🚀 Flask + PostgreSQL running in Docker Compose!"})

@app.route('/users')
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM users;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify({"users": rows})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
