import os
from flask import Flask, render_template_string

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    # Fetch the environment variable 'VARIABLE'
    variable_value = os.getenv('VARIABLE', 'Not Set')
    
    # Define a simple HTML template with the variable value
    html = f"""
    <html>
        <head>
            <title>Environment Variable Display</title>
        </head>
        <body>
            <h1>Environment Variable Value:</h1>
            <p>The value of the environment variable 'VARIABLE' is: <strong>{variable_value}</strong></p>
        </body>
    </html>
    """
    
    # Return the rendered HTML page
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
