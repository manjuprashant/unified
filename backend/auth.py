import os
import requests

from dotenv import load_dotenv
from fastapi import HTTPException
from jose import jwt

import os
from dotenv import load_dotenv

env_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "backend.env"
)

load_dotenv(env_path)

KEYCLOAK_URL = os.getenv("KEYCLOAK_URL")
REALM = os.getenv("KEYCLOAK_REALM")
CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID")

print("KEYCLOAK_URL =", KEYCLOAK_URL)
print("REALM =", REALM)
print("CLIENT_ID =", CLIENT_ID)


def get_public_key():

    url = (
        f"{KEYCLOAK_URL}/realms/"
        f"{REALM}/protocol/openid-connect/certs"
    )

    response = requests.get(url)

    response.raise_for_status()

    return response.json()


def verify_token(token: str):

    try:

        jwks = get_public_key()

        header = jwt.get_unverified_header(token)

        kid = header["kid"]

        key = None

        for item in jwks["keys"]:

            if item["kid"] == kid:
                key = item
                break

        if key is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        payload = jwt.decode(
            token,
            key,
            algorithms=["RS256"],
            options={
                "verify_aud": False
            }
        )

        return payload

    except Exception as error:

        raise HTTPException(
            status_code=401,
            detail=f"Authentication failed: {str(error)}"
        )