# Use an official Python runtime as a base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the working directory
COPY requirements.txt ./

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app listens on
EXPOSE 8000

# Specify the command to run the application when the container starts
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
