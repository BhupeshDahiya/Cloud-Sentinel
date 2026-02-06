# Use a lightweight Python base image
FROM python:3.11-slim

ARG CACHEBUST=1
# Create a non-root user and group usinf a specific UID/GID (1000) for consistency
# Create user first to use later and save some space on container
RUN groupadd -r appgroup && useradd -r -g appgroup -u 1000 appuser

WORKDIR /app

# Install the application dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code WITH ownership (Prevents image bloat)
# This replaces the need for a separate "RUN chown" command
COPY --chown=appuser:appgroup app.py .
COPY --chown=appuser:appgroup templates/ templates/

# Expose the port the app runs on
EXPOSE 5000

#Switch to the non-root user
USER appuser

# Command to run the app
CMD ["python", "app.py"]