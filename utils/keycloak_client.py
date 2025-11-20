import os
import requests
from config.configs import settings


class KeycloakClient:
    def __init__(self):
        self.base_url = settings.KEYCLOAK_BASE_URL
        self.realm = settings.KEYCLOAK_REALM
        self.client_id =  settings.KEYCLOAK_CLIENT_ID
        self.client_secret =  settings.KEYCLOAK_CLIENT_SECRET


    def get_token(self, username, password):
        url = f"{self.base_url}/realms/{self.realm}/protocol/openid-connect/token"

        data = {
            "grant_type": "password",
            "client_id": self.client_id,
            "username": username,
            "password": password,
        }

        if self.client_secret:
            data["client_secret"] = self.client_secret

        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json()

    def get_refresh_token(self, refresh_token):
        url = f"{self.base_url}/realms/{self.realm}/protocol/openid-connect/token"

        data = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "refresh_token": refresh_token,
        }

        if self.client_secret:
            data["client_secret"] = self.client_secret

        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json()
