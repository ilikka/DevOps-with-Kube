import hashlib
from datetime import datetime
import logging

from flask import Flask, render_template_string

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    pseudo_random = datetime.now().strftime('%Y-%m-%d-%s-%H:%M')
    hash_object = hashlib.sha256(pseudo_random.encode())
    current_datetime = datetime.now()
    datetime_str = str(current_datetime.strftime('%Y-%m-%d %H:%M.%S') )
    hash_hex = hash_object.hexdigest()

    # Define a simple HTML template with the variable value
    html = f"""
    <html>
        <head>
            <title>timestamp and string</title>
        </head>
        <body>
            <h1>timestamp and string:</h1>
            <p>{datetime_str} and string:  {hash_hex}</p>
        </body>
    </html>
    """
    
    # Return the rendered HTML page
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)










