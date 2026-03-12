# Boucheries du 44 - API Gateway / Core Service

This project serves as the API Gateway and Core Service for "Boucheries du 44", a platform designed to connect users with local butcheries. It provides RESTful APIs for user management and butchery information, along with a basic HTML frontend.

## Features

*   **User Management:**
    *   Register new users.
    *   User login and authentication (dummy JWT token).
    *   Retrieve user profiles.
*   **Butchery Management:**
    *   List all available butcheries.
    *   Get detailed information for a specific butchery.
    *   Search and filter butcheries (by query, latitude, longitude).
*   **Health Checks:**
    *   API Gateway health check.
    *   API v1 health check.

## Technologies

*   **Flask:** A lightweight WSGI web application framework for Python.

## Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd boucheries-du-44
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the application:**
    ```bash
    python app.py
    ```
    The API will be accessible at `http://127.0.0.1:5000/`.

## API Endpoints

### Health Checks
*   `GET /`: Returns `{"status": "API Gateway / Core Service is running"}`
*   `GET /api/v1/health`: Returns `{"status": "OK", "version": "1.0"}`

### User Service (`/api/v1/users`)
*   `POST /api/v1/users/register`: Register a new user.
    *   **Body:** `{"email": "...", "password": "..."}`
*   `POST /api/v1/users/login`: Log in a user.
    *   **Body:** `{"email": "...", "password": "..."}`
*   `GET /api/v1/users/profile/<user_id>`: Get a user's profile by ID.

### Butcheries Service (`/api/v1/butcheries`)
*   `GET /api/v1/butcheries/`: List all butcheries.
*   `GET /api/v1/butcheries/<butchery_id>`: Get details for a specific butchery by ID.
*   `GET /api/v1/butcheries/search?q=<query>&lat=<latitude>&lon=<longitude>`: Search for butcheries.

## Frontend

A basic HTML frontend is available at the root (`/`) of the application, serving `public/index.html`. It provides a welcome message and points to the API health endpoint.

---
*Developed as part of an AI-driven update.*