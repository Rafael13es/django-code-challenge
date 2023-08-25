#!/bin/bash
echo "Creating Migrations..."
python manage.py makemigrations planets
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Population database with SWAPI GraphQL"
python manage.py populate_planets
echo ====================================

echo "Starting Server..."
python manage.py runserver 0.0.0.0:8000