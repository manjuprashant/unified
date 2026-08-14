from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import dotenv_values
import os

env_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "backend.env"
)

config = dotenv_values(env_path)

print("ENV FILE:", env_path)
print("CONFIG:", config)

DATABASE_URL = config.get("DATABASE_URL")

print("DATABASE_URL:", DATABASE_URL)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()