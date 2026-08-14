# Unified User Provisioning Setup Guide

## Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL
- Keycloak
- Git

---

# 1. Clone Repository

```bash
git clone https://github.com/<your-username>/unified-user-provisioning.git
cd unified-user-provisioning
```

---

# 2. Backend Setup

Navigate to backend:

```bash
cd backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create environment file:

```env
DATABASE_URL=postgresql://admin:admin123@localhost:5432/unified_provisioning

KEYCLOAK_URL=http://localhost:8080
KEYCLOAK_REALM=unified-provisioning
KEYCLOAK_CLIENT_ID=react-client

JIRA_URL=https://your-domain.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your-api-token

GITHUB_TOKEN=your-github-token
```

Run backend:

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://localhost:8000
```

---

# 3. PostgreSQL Setup

Create database:

```sql
CREATE DATABASE unified_provisioning;
```

Update DATABASE_URL if needed.

---

# 4. Keycloak Setup

Start Keycloak:

```bash
docker compose up -d
```

Admin Console:

```text
http://localhost:8080
```

Create Realm:

```text
unified-provisioning
```

Create Client:

```text
react-client
```

Configure:

Root URL:

```text
http://localhost:5173
```

Valid Redirect URIs:

```text
http://localhost:5173/*
http://localhost:5174/*
http://localhost:5175/*
http://localhost:5176/*
```

Web Origins:

```text
*
```

Create Test User:

```text
Username: testuser
Password: password123
```

---

# 5. Frontend Setup

Navigate to root project:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

Example URL:

```text
http://localhost:5173
```

---

# 6. Test Authentication

Login using:

```text
Username: testuser
Password: password123
```

---

# 7. Provision User

Select:

- Jira
- GitHub
- Slack

Click:

```text
Create User Accounts
```

Expected Response:

```json
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
```

---

# API Documentation

Swagger:

http://localhost:8000/docs

OpenAPI:

http://localhost:8000/openapi.json