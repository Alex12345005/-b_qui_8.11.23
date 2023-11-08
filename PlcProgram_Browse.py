import requests
import json

def plc_program_browse(api_token, var, mode):
    """
    Ruft die Methode PlcProgram.Browse auf, um Variablen und ihre Metadaten zu durchsuchen.

    Args:
        api_token (str): Der API-Token, der zur Authentifizierung verwendet wird.
        var (str): Der Name der zu durchsuchenden Variable oder der Datenblock.
        mode (str): Der Modus, der das Verhalten der Methode festlegt (z. B. "var" oder "children").

    Returns:
        str: Die API-Antwort als Text.
    """
    url = "https://192.168.10.61/api/jsonrpc"

    payload = json.dumps({
      "id": 0,
      "jsonrpc": "2.0",
      "method": "PlcProgram.Browse",
      "params": {
        "var": var,
        "mode": mode
      }
    })
    headers = {
        'Content-Type': 'application/json',
        'Content-Length': str(len(payload)),
        'Host': '192.168.10.61',
        'X-Auth-Token': api_token
    }

    response = requests.post(url, headers=headers, data=payload, verify=False)
    return response.text
