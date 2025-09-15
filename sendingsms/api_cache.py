from django.core.cache import cache
import requests


def get_api_key():

    access_token = cache.get("access_token")
    if access_token is None:
        url_token = "https://api.orange.com/oauth/v3/token"
        payload = {
            "grant_type": "client_credentials"
        }
        headers = {
            "Authorization": "Basic Zk9jVDdoaUpaOURyb1pwZ3k0R2Q5RlA3amMxQUh0dkQ6M0p4a3dyNDNoc3NobXlMMQ==",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        }
        response = requests.post(url_token, data=payload, headers=headers)
        access_token = response.json()["access_token"]
        print(access_token)
        cache.set("access_token", access_token, timeout=3600)
    
    return access_token