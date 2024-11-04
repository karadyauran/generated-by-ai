# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY src/ ./src/

# Set the environment variables
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python", "src/main.py"]