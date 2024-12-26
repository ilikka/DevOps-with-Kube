import os 
import sys
from flask import Flask, render_template_string

# Initialize the Flask application
app = Flask(__name__)


@app.route('/')
def index():
    directory = os.getenv('FILE_DIRECTORY', './')  
    file_name = os.getenv('FILE_NAME', 'output.txt')  

    file_path = os.path.join(directory, file_name)    
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        file_content = f"Error: File '{file_path}' not found."
    except Exception as e:
        file_content = f"Error: {str(e)}"
        sys.exit(1) 


    
    html = f"""
    <html>
        <head>
            <title>timestamp and string</title>
        </head>
        <body>
            <h1>timestamp and string:</h1>
            <pre>{file_content}</pre>
        </body>
    </html>
    """
    
    # Return the rendered HTML page
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)










