from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Conectar a PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        dbname="mydatabase",
        user="admin",
        password="admin123",
        host="db"  # Nombre del servicio en docker-compose
    )
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify({"message": "Conexión exitosa", "server_time": result[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
