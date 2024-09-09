# apps/server/Dockerfile
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY apps/server/assignment/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY apps/server/assignment /app/

# Expose the port Django will run on
EXPOSE 8000

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
