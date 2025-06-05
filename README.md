# Modern Todo List Application

A sleek and responsive web-based Todo List application built with a microservices architecture. This application allows users to manage their tasks efficiently with features like adding, completing, and deleting todos, all presented in a modern and user-friendly interface.

## 🚀 Features

- Create new tasks
- Mark tasks as complete/incomplete
- Delete tasks
- Timestamp tracking for each task
- Responsive design for mobile and desktop
- Modern UI with smooth animations
- Empty state handling

## 🏗️ Architecture

The application follows a microservices architecture with two main services:

```
┌─────────────────┐      ┌─────────────────┐
│   Web Service   │      │ Database Service │
│    (Flask)      │◄────►│   (PostgreSQL)  │
└─────────────────┘      └─────────────────┘
```

### Web Service
- Handles HTTP requests
- Renders templates
- Manages business logic
- Provides REST API endpoints
- Communicates with database service

### Database Service
- Stores todo items
- Manages data persistence
- Handles data queries
- Ensures data integrity

## 💻 Tech Stack

### Web Service (Backend)
- **Framework**: Flask 3.0.2
- **Language**: Python 3.9
- **ORM**: SQLAlchemy 3.1.1
- **Template Engine**: Jinja2
- **Environment Management**: python-dotenv 1.0.1

### Database Service
- **Database**: PostgreSQL 13
- **Driver**: psycopg2-binary 2.9.9
- **Connection Pooling**: Built-in PostgreSQL connection pooling

### Frontend
- **HTML5**
- **CSS3** with modern features:
  - Flexbox
  - CSS Variables
  - Media Queries
  - Transitions & Animations
- **Font Awesome** for icons

## 🐳 Docker Configuration

The application is containerized using Docker with two services:

1. Web Container:
   - Python 3.9-slim base image
   - Exposed port: 5000
   - Health check enabled
   - Production-ready configuration

2. Database Container:
   - PostgreSQL 13
   - Exposed port: 5432
   - Persistent volume storage
   - Custom configuration support


## 🛠️ Project Structure

```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Web service container configuration
├── Dockerfile.postgres   # Database service container configuration
├── docker-compose.yml    # Services orchestration
├── static/
│   └── css/
│       └── style.css     # Application styles
└── templates/
    └── index.html        # Main template
```

## 🔐 Security

- SQL injection prevention through SQLAlchemy ORM
- CSRF protection built into Flask-WTF
- Secure database connection with SSL support

## 🔄 Continuous Integration

The application includes health checks for both services:
- Web service: HTTP endpoint check
- Database service: PostgreSQL connection check

