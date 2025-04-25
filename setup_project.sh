#!/bin/bash

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create Django project
django-admin startproject ticket_booking .

# Create apps
python manage.py startapp accounts
python manage.py startapp shows
python manage.py startapp bookings
python manage.py startapp admin_panel

# Create necessary directories
mkdir -p static/css
mkdir -p static/js
mkdir -p static/images
mkdir -p templates/accounts
mkdir -p templates/shows
mkdir -p templates/bookings
mkdir -p templates/admin_panel

# Create .env file
cat > .env << EOL
DEBUG=1
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgres://postgres:postgres@db:5432/ticket_booking
EOL

echo "Project setup complete!" 