# Ticket Booking Management System

A full-stack Django application for managing ticket bookings for shows and events.

## Features

- User Authentication (Registration, Login, Logout)
- View available shows/events
- Book tickets with seat selection
- Booking history
- Custom Admin Panel for show management

## Tech Stack

- Backend: Django 5.0.2
- Database: PostgreSQL
- Frontend: HTML, CSS, JavaScript
- Containerization: Docker
- CI/CD: Jenkins

## Setup & Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ticket-booking
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Run with Docker:
```bash
docker-compose up --build
```

4. Run migrations:
```bash
docker-compose run web python manage.py migrate
```

5. Create superuser:
```bash
docker-compose run web python manage.py createsuperuser
```

The application will be available at http://localhost:8000

## Project Structure

```
ticket_booking/
├── accounts/          # User authentication app
├── shows/            # Shows and events management
├── bookings/         # Ticket booking functionality
├── admin_panel/      # Custom admin interface
└── static/           # Static files
```

## Docker & Jenkins Usage

### Docker
- Build: `docker-compose build`
- Run: `docker-compose up`
- Stop: `docker-compose down`

### Jenkins
The Jenkinsfile includes:
- Build stage
- Test stage
- Deploy stage

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 