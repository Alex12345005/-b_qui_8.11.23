import requests
import json

def authenticate():
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
