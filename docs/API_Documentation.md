# Unified User Provisioning API

## Base URL

http://localhost:8000

---

## Authentication

All protected endpoints require:

```http
Authorization: Bearer <access_token>
```

Tokens are issued by Keycloak.

---

# Endpoints

## Health Check

### GET /

Returns API status.

### Response

```json
{
  "message": "Unified User Provisioning API",
  "status": "running"
}
```

---

## Current User

### GET /api/me

Returns authenticated user information.

### Headers

```http
Authorization: Bearer <access_token>
```

### Response

```json
{
  "email": "testuser@example.com",
  "preferred_username": "testuser"
}
```

---

## Provision User

### POST /api/users/provision

Creates accounts across selected applications.

### Headers

```http
Authorization: Bearer <access_token>
Content-Type: application/json
```

### Request

```json
{
  "applications": [
    "jira",
    "github",
    "slack"
  ]
}
```

### Response

```json
{
  "user": "testuser@example.com",
  "results": {
    "jira": {
      "status": "success",
      "external_user_id": "jira-testuser@example.com",
      "message": "Jira provisioning simulated successfully"
    },
    "github": {
      "status": "success",
      "message": "GitHub provisioning workflow can be implemented here"
    },
    "slack": {
      "status": "success",
      "message": "Slack provisioning workflow can be implemented here"
    }
  }
}
```

---

## Error Response

```json
{
  "detail": "Authentication failed"
}
```

---

## OpenAPI Documentation

Swagger UI:

http://localhost:8000/docs

OpenAPI JSON:

http://localhost:8000/openapi.json