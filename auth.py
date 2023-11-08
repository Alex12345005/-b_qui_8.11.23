import requests
import json

def authenticate():
    """
    Authentifiziert den Benutzer über die API und erhält einen API-Token.

    Sendet eine Anfrage an die API, um den Benutzer zu authentifizieren und erhält einen API-Token
    zur weiteren Verwendung.

    Returns:
        str: Der erhaltene API-Token.
    """
    url = "https://192.168.10.61/api/jsonrpc"

    payload = json.dumps({
      "id": 0,
      "jsonrpc": "2.0",
      "method": "Api.Login",
      "params": {
        "user": "5AHIT",
        "password": "5ahiT"
      }
    })
    headers = {
        'Content-Type': 'application/json',
        'Content-Length': str(len(payload)),
        'Host': '192.168.10.61'
    }

    response = requests.post(url, headers=headers, data=payload, verify=False)
    return response.json()['result']['token']
