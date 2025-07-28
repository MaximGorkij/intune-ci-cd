import requests

def get_token(config):
    tenant = config["auth"]["tenantId"]
    client_id = config["auth"]["clientId"]
    secret = config["auth"]["clientSecret"]
    scope = config["auth"]["scope"]

    url = f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"
    data = {
        "client_id": client_id,
        "client_secret": secret,
        "scope": scope,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, data=data)
    return response.json()["access_token"]