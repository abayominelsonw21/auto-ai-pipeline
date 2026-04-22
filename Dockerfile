# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local files into the container
COPY . /app

# Install the necessary libraries
RUN pip install --no-cache-dir pandas streamlit xgboost joblib

# Expose the port Streamlit uses (8501)
EXPOSE 8501

# Command to launch the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]