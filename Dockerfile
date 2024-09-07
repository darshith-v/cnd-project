# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements and source code to the container
COPY requirements.txt requirements.txt
COPY . .

# Install the dependencies
RUN pip install -r requirements.txt

# Expose the port on which the app will run
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
