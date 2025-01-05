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

directory = os.getenv('FILE_DIRECTORY', './')  
file_name = os.getenv('FILE_NAME', 'out.put.txt')  

file_path = os.path.join(directory, file_name)


def read_or_create_file():
    if not os.path.exists(file_path):
        # File doesn't exist, so create it and write the default value
        with open(file_path, 'w') as file:
            file.write( '0' )
            logging.info(f"File '{file_path}' was created with the default value: 0")
            return 0
    else:
        # File exists, so read the value from it
        with open(file_path, 'r') as file:
            content = file.read().strip()  # Strip any extra whitespace/newlines
            try:
                logging.info(f"Value read from the file: {content}")
                return  int(content)
            except:
                logging.error(f"shit hit the fan - return default")
                return 1

def update_file(value):
    # Update the file with a new value (overwrite the old value)
    with open(file_path, 'w') as file:
        file.write(str(value))  # Store value as string
    print(f"File '{file_path}' updated with value: {value}")




# Define a route that listens to GET requests at the URL specified by the environment variable
@app.route(ping_path, methods=['GET'])
def pong():
    
    request_counter = read_or_create_file()
    request_counter  += 1 
    update_file(request_counter)
    logging.info(f"request counter: '{request_counter}' ")
    return f"pong {request_counter}", 200


# Default route to catch all undefined URLs and return a custom "Not Found" message
@app.route('/<path:path>', methods=['GET'])
def not_found(path):
    return jsonify(error="Not Found", message=f"The URL '/{path}' is not recognized."), 404

# Run the server
if __name__ == "__main__":
    print(f"Running on {host}:{port}{ping_path}...")
    app.run(host=host, port=port)
