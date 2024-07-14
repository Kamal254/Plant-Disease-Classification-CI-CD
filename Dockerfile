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

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
COPY models/ /app/models/

RUN ls -la $APP_HOME/
RUN ls -la /app/models/

# Install dependencies
RUN pip install -r requirements.txt

# Run the streamlit on container startup
CMD ["streamlit", "run", "--server.enableCORS", "false", "imgwebapp.py"]
