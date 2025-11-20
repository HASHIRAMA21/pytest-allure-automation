import allure

@allure.feature("Auth Flow")
@allure.story("Keycloak login + token refresh ")
def test_keycloak_auth_flow(keycloak):
    with allure.step("Get an access token"):
        token = keycloak.get_token("admin","admin")
        allure.attach(str(token), "Access Token")
        assert "access_token" in token

    with allure.step("Refresh token"):
        refresh_token = keycloak.get_refresh_token(token['refresh_token'])
        allure.attach(str(refresh_token), "Refresh Token")
        assert "refresh_token" in refresh_token
