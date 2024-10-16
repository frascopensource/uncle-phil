# Use an official Python image as the base
FROM python:3.10.15-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements
COPY ./requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY ./src /app

# Expose the port that Streamlit runs on (8501)
EXPOSE 8501

# Set the environment variable to avoid running in interactive mode
ENV PYTHONUNBUFFERED=1

# Command to run the Streamlit app
CMD ["streamlit", "run", "main.py"]
