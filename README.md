# Event Management and RSVP System
A Django REST framework-based application that allows users to sign up, log in, view events, RSVP to events, and manage their event engagements. This project demonstrates custom user authentication, RESTful API design, and token-based authentication with Django.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Getting Started](#getting-started)
5. [API Endpoints](#api-endpoints)
6. [Future Enhancements](#future-enhancements)

## Project Overview
This application provides a simple event management system where users can register for events and RSVP to attend them. It demonstrates custom user model creation, user authentication using Django REST framework’s token authentication, and CRUD operations on event data. This project is suitable for showcasing Django skills, RESTful API design, and user authentication.
## Features
- User registration and login using a custom user model
- Token-based authentication for secure API access
- View all available events
- RSVP to events and manage user-specific RSVP status
- View events the user has RSVP’d to

## Technologies Used
- **Backend:** Django, Django REST Framework
- **Database:** SQLite (for development; can be switched to PostgreSQL for production)
- **Authentication:** Custom user model with Token-based authentication
- **API Documentation:** JSON responses for all endpoints

## Getting Started
### Prerequisites
- Python 3.8+
- Django 4.0+
- Django REST Framework

## Installation
#### 1. Clone the repository:
```bash
git clone https://github.com/brijesh-13/EventManagement.git
cd event_manager
```

#### 2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

#### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

#### 4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5. Create a superuser (for accessing Django Admin and managing events):
```bash
python manage.py createsuperuser
```

#### 6. Start the server:
```bash
python manage.py runserver
```

#### 7. Testing the API: Use a tool like Postman or curl to test the API endpoints


## API Endpoints
### User Authentication
**- Signup:** ```POST /api/signup/```
- Payload: { "email": "user@example.com", "username": "username", "password": "password" }
- Creates a new user

**- Login:** ```POST /api/login/```
- Payload: { "email": "user@example.com", "password": "password" }
- Returns an authentication token

### Event Management
**- List All Events:** ```GET /api/events/```
- Requires authentication
- Returns a list of all events

**- Create Event:** ```POST /api/events/```
- Requires authentication and organizer privileges
- Payload: { "title": "Event Title", "description": "Event Description", "location": "Location", "date": "YYYY-MM-DDTHH:MM:SSZ" }

**- RSVP to Event:** ```POST /api/events/<event_id>/rsvp/```
- Requires authentication
- Adds the user’s RSVP to the specified event

**- View User's RSVPs:** ```GET /api/user/rsvps/```
- Requires authentication
- Returns a list of events the user has RSVP’d to

## Future Enhancements
- **Email Notifications:** Notify users upon successful RSVP
- **Event Comments:** Allow users to comment on events
- **Event Capacity Management:** Set and manage attendance limits for events
- **User Profiles:** Enhance user profiles with more details and profile pictures
