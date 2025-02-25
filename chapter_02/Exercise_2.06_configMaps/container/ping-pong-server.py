import os
import logging
from flask import Flask, jsonify


# Create a Flask application
app = Flask(__name__)

# Read environment variables with defaults
ping_path = os.getenv('PING_PATH', '/ping')
host = os.getenv('FLASK_HOST', '0.0.0.0')
port = int(os.getenv('FLASK_PORT', 5000))

logging.basicConfig(level=logging.INFO, format='%(message)s')

request_counter = 0 


# Define a route that listens to GET requests at the URL specified by the environment variable
@app.route(ping_path, methods=['GET'])
def pong():
    
    global request_counter
    request_counter  += 1 
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
