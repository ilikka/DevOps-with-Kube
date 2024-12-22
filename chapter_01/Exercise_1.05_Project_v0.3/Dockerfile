# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the app files to the container
COPY front_app.py .

# Install Flask
RUN pip install Flask

# Set the environment variable (optional, if you want to set the default value here)
ENV VARIABLE="Hello from Docker!"

# Expose the port that Flask uses
EXPOSE 5000

# Run the app
CMD ["python", "front_app.py"]
