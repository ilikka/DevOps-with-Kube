# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the app files to the container
COPY ping-pong-server.py .

# Install Flask
RUN pip install Flask jsonify python-dotenv 


# Expose the port that Flask uses
EXPOSE 3000

# Run the app
CMD ["python", "ping-pong-server.py"]
