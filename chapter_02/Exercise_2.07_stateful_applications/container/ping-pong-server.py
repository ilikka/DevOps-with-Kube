import os
import logging
from flask import Flask, jsonify
import psycopg2


# Create a Flask application
app = Flask(__name__)

# Database connection parameters
DB_HOST = os.getenv('DB_HOST','postgres-service.devops-ns.svc.cluster.local')  # Change if needed
DB_PORT = "5432"
DB_NAME = "devopsdb"
DB_USER = "admin"
DB_PASSWORD = "password"

# Read environment variables with defaults
ping_path = os.getenv('PING_PATH', '/ping')
host = os.getenv('FLASK_HOST', '0.0.0.0')
port = int(os.getenv('FLASK_PORT', 5000))

logging.basicConfig(level=logging.INFO, format='%(message)s')

def get_nextval():
    """Fetch the next value of the sequence from PostgreSQL."""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        cur.execute("SELECT nextval('select_counter_seq');")
        result = cur.fetchone()[0]  # Get the first column of the first row
        cur.close()
        conn.close()
        return result
    except Exception as e:
        return str(e)


# Define a route that listens to GET requests at the URL specified by the environment variable
@app.route(ping_path, methods=['GET'])
def pong():
    """Handle GET requests and return the next sequence value."""
     
    request_counter  = get_nextval()
    logging.info(f"request counter: '{request_counter}' ")
    return f"{request_counter}", 200

# Default route to catch all undefined URLs and return a custom "Not Found" message
@app.route('/<path:path>', methods=['GET'])
def not_found(path):
    return jsonify(error="Not Found", message=f"The URL '/{path}' is not recognized."), 404

# Run the server
if __name__ == "__main__":
    print(f"Running on {host}:{port}{ping_path}...")
    app.run(host=host, port=port)
