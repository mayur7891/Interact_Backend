# Use the official Python image as base
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . .

# Expose the port Flask will run on (Cloud Run requires 8080)
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]
