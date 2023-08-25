# Use an official Python runtime as a parent image
FROM python:3.10-alpine

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=planets_crud.settings

# Create and set the working directory
RUN mkdir /app
WORKDIR /app/planets_crud/

# Install project dependencies
COPY requirements.txt /app/planets_crud/
COPY django.sh /app/planets_crud/
RUN pip install -r requirements.txt
RUN chmod +x /app/planets_crud/django.sh

# Copy the project files into the container
COPY ./planets_crud /app/planets_crud/

RUN export PYTHONPATH=/app/planets_crud

# Expose port
EXPOSE 8000

# entrypoint to run the django.sh file
ENTRYPOINT ["sh", "/app/planets_crud/django.sh"]