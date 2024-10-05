# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV MICROSOFT_APP_ID=xxx
ENV MICROSOFT_APP_PASSWORD=yyyy
ENV AZURE_OPENAI_ENDPOINT=zzz
ENV AZURE_OPENAI_KEY=aaa
ENV PORT=3978

# Create and set the working directory
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE $PORT

# Define the command to run the application
CMD ["python", "app.py"]
