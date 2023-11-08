import requests
import json

def getpermissions(api_token):
    """
    Ruft die Benutzerberechtigungen über die API ab.

    Sendet eine Anfrage an die API, um die Berechtigungen des Benutzers abzurufen.

    Args:
        api_token (str): Der API-Token, der zur Authentifizierung verwendet wird.

    Returns:
        str: Die API-Antwort als Text.
    """
    url = "https://192.168.10.61/api/jsonrpc"

    payload = json.dumps({
      "id": 0,
      "jsonrpc": "2.0",
      "method": "Api.GetPermissions"
    })
    headers = {
        'Content-Type': 'application/json',
        'Content-Length': str(len(payload)),
        'Host': '192.168.10.61',
        'X-Auth-Token': api_token
    }

    response = requests.post(url, headers=headers, data=payload, verify=False)
    return response.text
