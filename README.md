# Unified User Provisioning System

A full-stack user provisioning platform that integrates authentication with Keycloak and automates user onboarding across multiple enterprise applications such as Jira, GitHub, and Slack.

---

## Project Overview

This project provides a centralized portal where users can:

- Authenticate using Keycloak Single Sign-On (SSO)
- Select target applications
- Provision accounts automatically
- Store provisioning history in PostgreSQL
- Manage enterprise onboarding workflows from a single interface

---

## Features

### Authentication

- Keycloak Integration
- OpenID Connect (OIDC)
- JWT Token Validation
- Single Sign-On (SSO)

### User Provisioning

- Jira User Provisioning
- GitHub User Provisioning
- Slack User Provisioning
- Extensible Application Connectors

### Database Management

- PostgreSQL Storage
- User Records
- Provisioning Audit Logs
- Provisioning Status Tracking

### API

- FastAPI Backend
- OpenAPI Documentation
- Swagger UI
- RESTful Architecture

### Frontend

- React + Vite
- Keycloak Login
- Application Selection Interface
- Provisioning Status Dashboard

---

# Technology Stack

## Frontend

- React
- Vite
- JavaScript
- Keycloak JS

## Backend

- FastAPI
- SQLAlchemy
- Python
- Pydantic

## Authentication

- Keycloak
- OpenID Connect (OIDC)
- JWT

## Database

- PostgreSQL

## DevOps

- Docker
- Docker Compose

---

# Architecture

User
↓
React Frontend
↓
Keycloak Authentication
↓
FastAPI Backend
↓
Provisioning Engine
↓
Jira / GitHub / Slack

Database:
PostgreSQL

---

# Project Structure

unified-user-provisioning/

├── backend/

│ ├── main.py

│ ├── auth.py

│ ├── database.py

│ ├── models.py

│ ├── provisioning.py

│ ├── backend.env

│ └── requirements.txt

│

├── src/

│ ├── App.jsx

│ ├── main.jsx

│ ├── keycloak.js

│ └── App.css

│

├── docs/

│ ├── Architecture_Diagram.png

│ ├── API_Documentation.md

│ └── Setup_Guide.md

│

├── screenshots/

│ ├── login-page.png

│ ├── keycloak-admin.png

│ ├── provisioning-success.png

│ └── swagger-ui.png

│

├── docker-compose.yaml

├── package.json

├── index.html

└── README.md

---

# Database Schema

## Users Table

| Column | Type |
|----------|---------|
| id | Integer |
| keycloak_user_id | String |
| first_name | String |
| last_name | String |
| email | String |

## Provisioning Table

| Column | Type |
|----------|---------|
| id | Integer |
| email | String |
| application | String |
| status | String |
| external_user_id | String |
| message | Text |

---

# API Endpoints

## Health Check

GET /

Response:

{
  "message": "Unified User Provisioning API",
  "status": "running"
}

---

## Current User

GET /api/me

Returns authenticated user details.

---

## Provision User

POST /api/users/provision

Request:

{
  "applications": [
    "jira",
    "github",
    "slack"
  ]
}

Response:

{
  "user": "testuser@example.com",
  "results": {
    "jira": {
      "status": "success"
    },
    "github": {
      "status": "success"
    },
    "slack": {
      "status": "success"
    }
  }
}

---

# Environment Variables

backend.env

DATABASE_URL=postgresql://admin:admin123@localhost:5432/unified_provisioning

KEYCLOAK_URL=http://localhost:8080

KEYCLOAK_REALM=unified-provisioning

KEYCLOAK_CLIENT_ID=react-client

JIRA_URL=https://your-domain.atlassian.net

JIRA_EMAIL=your-email@example.com

JIRA_API_TOKEN=your-api-token

GITHUB_TOKEN=your-github-token

---

# Installation

## Clone Repository

git clone https://github.com/your-username/unified-user-provisioning.git

cd unified-user-provisioning

---

## Install Backend Dependencies

cd backend

pip install -r requirements.txt

---

## Start Backend

uvicorn main:app --reload

Backend URL:

http://localhost:8000

Swagger UI:

http://localhost:8000/docs

---

## Install Frontend Dependencies

npm install

---

## Start Frontend

npm run dev

Frontend URL:

http://localhost:5173

---

# Keycloak Setup

1. Create Realm

unified-provisioning

2. Create Client

react-client

3. Configure Redirect URIs

http://localhost:5173/*

http://localhost:5174/*

http://localhost:5175/*

http://localhost:5176/*

4. Create Test User

Username:

testuser

Email:

testuser@example.com

Password:

password123

---

# Screenshots

- Login Page
- Keycloak Admin Console
- Provisioning Dashboard
- Swagger API Documentation

---

# Future Enhancements

- Microsoft Entra ID Integration
- Okta Integration
- SCIM Provisioning
- Role-Based Access Control (RBAC)
- Approval Workflows
- Audit Dashboard
- Email Notifications
- Kubernetes Deployment

---

# Author

Manjula Srinivasan

AI & DevOps Intern — Springer Capital

Data Analytics Intern — Infotact Solutions

Data Science & Machine Learning Intern — Zaalima Pvt Ltd

2026
