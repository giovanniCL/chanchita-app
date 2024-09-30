import os
from dotenv import load_dotenv

load_dotenv()

# APPLICATION
SERVER_HOST = os.environ.get("SERVER_HOST", "0.0.0.0")
SERVER_PORT = os.environ.get("SERVER_PORT", 8080)
DEBUG = os.environ.get("DEBUG", False)


# DATABASE
HOST = os.environ.get("DB_HOST")
PORT = os.environ.get("DB_PORT")
DB = os.environ.get("DB_NAME")
USER = os.environ.get("DB_USER")
PASSWORD = os.environ.get("DB_PASSWORD")
ENGINE = "sqlite"

# JWT
JWT_SECRET = os.environ.get("JWT_SECRET")