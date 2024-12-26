# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the app files to the container
COPY logoutput_app.py .

# Install Flask
RUN pip install Flask


# Expose the port that Flask uses
EXPOSE 3000

# Run the app
CMD ["python", "logoutput_app.py"]
