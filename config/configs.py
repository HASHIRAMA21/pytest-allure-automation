import os


class Settings:
    KEYCLOAK_BASE_URL = "http://localhost:8080"
    KEYCLOAK_REALM = "master"
    KEYCLOAK_CLIENT_ID = "admin-cli"
    KEYCLOAK_CLIENT_SECRET = ""
    KEYCLOAK_USERNAME = "admin"
    KEYCLOAK_PASSWORD = "admin"
    API_BASE_URL = "http://localhost:8000"

settings = Settings()

