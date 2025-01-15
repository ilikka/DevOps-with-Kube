import os
import time
import logging
import requests 
from flask import Flask, render_template_string, request,  redirect, url_for


# Initialize Flask app
app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(message)s')
# The URL of the image to fetch
image_url = "https://picsum.photos/1200.jpg"  # Replace with your image URL
directory = os.getenv('FILE_DIRECTORY', './')  
file_name = os.getenv('FILE_NAME', 'output.txt')  
base_url = os.getenv('BASE_URL', '/')
submitted_todos = []
submit_url = os.getenv('SUBMIT_URL', '/todos')


html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Page with Dynamic Image and Text Field</title>
    <script>
        // This function will fetch the data from the /todos route and update the page
        function fetchData() {
            fetch('/todos')
                .then(response => response.json())  // Parse the JSON response
                .then(data => {
                    // Populate the list in the HTML with data
                    const listElement = document.getElementById('todos');
                    listElement.innerHTML = '';  // Clear any previous content
                    data.forEach(item => {
                        const listItem = document.createElement('li');
                        listItem.textContent = `${item.id}: ${item.text}`;
                        listElement.appendChild(listItem);
                    });
                })
                .catch(error => console.error('Error fetching data:', error));
        }

        // Wait for the DOM to fully load before fetching data
        window.onload = fetchData;
    </script>
</head>
<body>
    <!-- Display an image with dynamically set src -->
    <img src="{{ file_path }}" alt="Sample Image" width="400">

    <h2>Enter Text and Submit</h2>
    
    <!-- Simple form with text input field and submit button -->
    <form action="{{ submit_url }}" method="POST">
        <input type="text" name="userInput" maxlength=140 placeholder="Enter something" required>
        <button type="submit">Submit</button>
    </form>

    <h3>All Submitted Entries:</h3>
    <ul id="todos">
        <!-- List items will be dynamically inserted here -->
    </ul>


</body>
</html>
"""


# Directory to save the images
save_dir = os.getenv('IMAGE_DIR', 'static/images')
image_name = os.getenv('IMAGE_NAME', 'tmp.jpg')

# Ensure the directory exists
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

def fetch_and_save_image(url):
    try:
        # Send HTTP GET request to fetch the image
        response = requests.get(url)
        logging.info(f"get image response code: {response} ")
        if response.status_code == 200:
            file_path = os.path.join(save_dir, image_name)
            # Save the image to a file
            with open(file_path, 'wb') as file:
                file.write(response.content)
                logging.info(f"save image : {file_path}")
        else:
            logging.info(f"Failed to fetch image. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred: {e}")

@app.route('/', methods=['GET'])
def index():
    # Get the latest image file in the directory
    file_path = os.path.join(save_dir, image_name)
    logging.info(f"image path: {file_path}")
    logging.info(f"todo list : {submitted_todos}")
    return render_template_string(html_content, file_path=file_path, submit_url=submit_url, submitted_todos=submitted_todos )
 



def main():
    # Fetch image every 60 minutes
    while True:
        fetch_and_save_image(image_url)
        print(f"Waiting for 60 minutes before fetching again...")
        time.sleep(36)  # Wait for 60 minutes (3600 seconds)

if __name__ == "__main__":
    from threading import Thread
    
    # Run the Flask web server in a separate thread
    flask_thread = Thread(target=app.run, kwargs={'debug': True, 'use_reloader': False, 'host': '0.0.0.0', 'port': 3000 })
    flask_thread.start()
    
    # Run the image fetching function in the main thread
    main()
