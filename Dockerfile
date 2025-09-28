# Stage 1: Build frontend
FROM node:22 AS frontend-builder
WORKDIR /app/client

COPY client/ .

RUN npm install
RUN npx vite build

# Stage 2: Build backend
FROM python:3.11-slim

# Create working directory
WORKDIR /app

# Copy backend source code
COPY app.py .
COPY src/ ./src
COPY templates ./templates

# Set the PYTHONPATH so Python can find `src/hologram_project`
ENV PYTHONPATH="/app/src"

# Install backend dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy built frontend files into backend's static directory
COPY --from=frontend-builder /app/client/static/assets ./client/static/assets

# Set environment variables
ENV FLASK_APP=app:app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["flask", "run"]
