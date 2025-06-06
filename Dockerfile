# Use Official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR / app

# Copy Project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

