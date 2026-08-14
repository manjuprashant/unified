from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    keycloak_user_id = Column(
        String,
        unique=True,
        nullable=False
    )

    first_name = Column(String)

    last_name = Column(String)

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class Provisioning(Base):

    __tablename__ = "provisioning"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String)

    application = Column(String)

    status = Column(String)

    external_user_id = Column(String, nullable=True)

    message = Column(String, nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )