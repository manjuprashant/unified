from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from database import engine, Base, SessionLocal
from models import User, Provisioning
from auth import verify_token
from provisioning import provision_user

from pydantic import BaseModel
from typing import List


# Create database tables

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Unified User Provisioning API",
    version="1.0.0"
)


# --------------------------------
# CORS
# --------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
        "http://localhost:5176"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# --------------------------------
# Request model
# --------------------------------

class ProvisionRequest(BaseModel):

    applications: List[str]


# --------------------------------
# Health check
# --------------------------------

@app.get("/")
def root():

    return {
        "message": "Unified User Provisioning API",
        "status": "running"
    }


# --------------------------------
# Current user
# --------------------------------

@app.get("/api/me")
def get_current_user(
    authorization: str = Header(None)
):

    if not authorization:

        raise HTTPException(
            status_code=401,
            detail="Authorization header missing"
        )

    token = authorization.replace(
        "Bearer ",
        ""
    )

    user = verify_token(token)

    return user


# --------------------------------
# Provision user
# --------------------------------

@app.post("/api/users/provision")
def provision(
    request: ProvisionRequest,
    authorization: str = Header(None)
):

    if not authorization:

        raise HTTPException(
            status_code=401,
            detail="Authorization header missing"
        )

    token = authorization.replace(
        "Bearer ",
        ""
    )

    keycloak_user = verify_token(token)

    email = keycloak_user.get("email")

    first_name = keycloak_user.get(
        "given_name",
        ""
    )

    last_name = keycloak_user.get(
        "family_name",
        ""
    )

    keycloak_id = keycloak_user.get("sub")


    user_data = {

        "email": email,

        "first_name": first_name,

        "last_name": last_name,

        "keycloak_user_id": keycloak_id
    }


    db: Session = SessionLocal()


    try:

        existing_user = db.query(User).filter(
            User.email == email
        ).first()


        if not existing_user:

            new_user = User(
                keycloak_user_id=keycloak_id,
                first_name=first_name,
                last_name=last_name,
                email=email
            )

            db.add(new_user)

            db.commit()

        results = provision_user(
            user_data,
            request.applications
        )


        for application, result in results.items():

            record = Provisioning(

                email=email,

                application=application,

                status=result.get("status"),

                external_user_id=result.get(
                    "external_user_id"
                ),

                message=result.get("message")
            )

            db.add(record)


        db.commit()


        return {

            "user": email,

            "results": results

        }

    finally:

        db.close()