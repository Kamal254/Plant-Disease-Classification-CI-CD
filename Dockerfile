# # lightweight python
# FROM python:3.7-slim

# RUN apt-get update

# # Copy local code to the container image.
# ENV APP_HOME /app
# WORKDIR $APP_HOME
# COPY . ./

# RUN ls -la $APP_HOME/

# # Install dependencies
# RUN pip install -r requirements.txt

# # Run the streamlit on container startup
# CMD [ "streamlit", "run","--server.enableCORS","false","imgwebapp.py" ]


# Lightweight python
FROM python:3.7-slim

RUN apt-get update

# Set environment variables
ENV APP_HOME=/app

# Create application directory
WORKDIR $APP_HOME

# Copy all files to the container
COPY . ./

# List files in the application directory
RUN ls -la $APP_HOME/
RUN ls -la $APP_HOME/models/

# Install dependencies
RUN pip install -r requirements.txt

# Run the streamlit on container startup
CMD ["streamlit", "run", "--server.enableCORS", "false", "imgwebapp.py"]


