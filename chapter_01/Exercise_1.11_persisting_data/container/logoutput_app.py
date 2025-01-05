import os 
import sys
import hashlib
import logging
import requests
from flask import Flask, render_template_string
from datetime import datetime


# Initialize the Flask application
app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(message)s')
directory = os.getenv('FILE_DIRECTORY', './')  
file_name = os.getenv('FILE_NAME', 'out.put.txt')  
file_path = os.path.join(directory, file_name)    
serveri = os.getenv('BACKEND_URL', 'http://server:5000' )

def make_request():
    response = requests.get(serveri)  # 'server' is the name of the Kubernetes service
    logging.info(f"make_request response sring {response.text} ")



@app.route('/')
def index():
    make_request() 
    current_datetime = datetime.now()
    datetime_str = str(current_datetime.strftime('%Y-%m-%d %H:%M.%S') )

    hash_object = hashlib.sha256(datetime_str.encode())
    hash_hex = hash_object.hexdigest()



    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        file_content = f"Error: File '{file_path}' not found."
    except Exception as e:
        file_content = f"Error: {str(e)}"
        sys.exit(1) 

    logging.info(f"response sring {datetime_str} : {hash_hex} and pong {file_content}")
    
    html = f"""
    <html>
        <head>
            <title>timestamp and string</title>
        </head>
        <body>
            <h2>timestamp and string:</h2>
            <p> {datetime_str}: {hash_hex}  
            <pre>Ping / Pongs: {file_content}</pre>
        </body>
    </html>
    """
    
    # Return the rendered HTML page
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)










