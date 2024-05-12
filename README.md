# Freelancer Connect

## Introduction
Freelancer Connect is a platform designed to connect freelancers with potential clients, enhancing visibility and opportunities in Bangalore, India's tech hub. 

### Problem Statement
Bangalore is India's tech hub with a vast freelance workforce. Establish a platform that connects freelancers with potential clients, enhancing visibility and opportunities.

## Features
- **Freelancer Dashboard**: Allows freelancers to view potential projects and apply for them.
- **Client Dashboard**: Enables clients to post projects and view freelancer profiles.
- **Project Matching**: Uses an algorithm to match freelancers with suitable projects based on skills and experience.
- **Real-time Notifications**: Sends notifications to freelancers when new projects are posted or when a client shows interest in their profile.
- **Messaging System**: Facilitates communication between freelancers and clients for project discussions.

## Technology Stack
- **Frontend**:
  - React
  - HTML
  - CSS
  - JavaScript
  
- **Backend**:
  - Python
  - Flask
  
- **Database**:
  - PostgreSQL
  
- **Deployment**:
  - Heroku (Backend)
  - Netlify (Frontend)

## Configuration Details
### Frontend Configuration
- **React Environment Variables**:
  - REACT_APP_GEMINI_API_KEY: API key for the Gemini service.

### Backend Configuration
- **Flask Environment Variables**:
  - GEMINI_API_KEY: API key for the Gemini service.

## Installation
### Frontend
1. Clone the repository.
2. Navigate to the frontend directory.
3. Install dependencies using `npm install`.
4. Set the environment variable `REACT_APP_GEMINI_API_KEY` in a `.env` file.
5. Start the development server with `npm start`.

### Backend
1. Clone the repository.
2. Navigate to the backend directory.
3. Create a virtual environment using `python -m venv venv`.
4. Activate the virtual environment (`venv\Scripts\activate` on Windows, `source venv/bin/activate` on macOS/Linux).
5. Install dependencies using `pip install -r requirements.txt`.
6. Set the environment variable `GEMINI_API_KEY` (either using a `.env` file or directly in the environment).
7. Run the Flask application with `flask run`.

## Contributors
- [Shaik Mohammed Huzaifa]
