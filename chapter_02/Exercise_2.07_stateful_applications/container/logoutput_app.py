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
serveri = os.getenv('BACKEND_URL', 'http://server:5000' )
MSG_CONF = os.getenv('MESSAGE','Shit hit the fan')


def make_request():
    response = requests.get(serveri)  # 'server' is the name of the Kubernetes service
    logging.info(f"make_request response string {response.text} ")
    return  response.text


@app.route('/')
def index():
    count = make_request() 
    current_datetime = datetime.now()
    datetime_str = str(current_datetime.strftime('%Y-%m-%d %H:%M.%S') )

    hash_object = hashlib.sha256(datetime_str.encode())
    hash_hex = hash_object.hexdigest()


    logging.info(f"response sring {datetime_str} : {hash_hex} and pong {count}")
    logging.info(f"MESSAGE: {MSG_CONF}");  
    
    html = f"""
    <html>
        <head>
            <title>timestamp and string</title>
        </head>
        <body>
            <h2>timestamp and string:</h2>
            <p> file content: this text is from file </p> 
            <p> env variable: {MSG_CONF}
            <p> {datetime_str}: {hash_hex}  
            <pre>Ping / Pongs: {count}</pre>
        </body>
    </html>
    """
    
    # Return the rendered HTML page
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
