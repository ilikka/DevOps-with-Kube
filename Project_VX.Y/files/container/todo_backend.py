import os
import time
import logging
from flask import Flask, jsonify, request,  redirect, url_for


# Initialize Flask app
app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(message)s')
# The URL of the image to fetch
submitted_todos = []


@app.route('/todos', methods=['GET'])
def get_value():
    logging.info(f"todo list : {submitted_todos}")
    return submitted_todos, 200

@app.route( '/todos', methods=['POST'])
def submit_value():
    user_input = request.form.get ('userInput')
    logging.info(f"User input: {user_input}")
    if user_input: 
        item = {
        "id": len(submitted_todos) + 1,  # Just an example of auto-generating an ID
        "text": user_input,
        "completed": False
        }
        submitted_todos.append(item)
        logging.info(f"User input: {submitted_todos}")
    return redirect(url_for('index'))  
    # return jsonify(submitted_todos), 201  
 
@app.route('/', methods=['GET'] )
def index():
    logging.info('Dummy index for redirect. Ingres hopefully save us')
    return "Go to the homepage!"
    
# Catch-all route for wrong paths
@app.route('/<path:path>')
def handle_invalid_path(path):
    return jsonify(error=f"'{path}' not found"), 404

def main():
    logging.info('app started')

if __name__ == "__main__":
    from threading import Thread
    
    # Run the Flask web server in a separate thread
    flask_thread = Thread(target=app.run, kwargs={'debug': True, 'use_reloader': False, 'host': '0.0.0.0', 'port': 5005})
    flask_thread.start()
    main()

