FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt
# --no-cache-dir 

# Copy the application code to the container
COPY . .

# Expose the port on which the Flask server will run
EXPOSE 8181

# Set the entrypoint command to run the Flask server
CMD ["python3", "flask_chat_server.py"]