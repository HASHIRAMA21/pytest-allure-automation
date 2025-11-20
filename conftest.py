import os

import pytest
from dotenv import load_dotenv
from config.configs import settings
from utils.keycloak_client import KeycloakClient


@pytest.fixture(scope="session")
def keycloak():
    load_dotenv()
    return KeycloakClient()



@pytest.fixture(scope="session")
def access_token(keycloak):
    token = keycloak.get_token(
        settings.KEYCLOAK_USERNAME,
        settings.KEYCLOAK_PASSWORD
    )
    return token["access_token"]

@pytest.fixture()
def auth_header(access_token):
    return {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

@pytest.fixture(scope="session")
def load_env():
    load_dotenv()
    return os.environ



@pytest.fixture(scope="session")
def refresh_token(access_token):
    return {
        "refresh_token": access_token,
    }