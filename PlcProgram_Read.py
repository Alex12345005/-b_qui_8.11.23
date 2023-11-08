import requests
import json

def plc_program_read(api_token, var, mode="simple"):
    """
    Liest eine Variable aus einer CPU mit der Methode PlcProgram.Read.

    Args:
        api_token (str): Der API-Token, der zur Authentifizierung verwendet wird.
        var (str): Der Name der zu lesenden Variable.
        mode (str, optional): Der Modus, der das Antwortformat festlegt. Standardmäßig ist "simple".

    Returns:
        str: Die API-Antwort als Text.
    """
    url = "https://192.168.10.61/api/jsonrpc"

    payload = json.dumps({
        "id": 0,
        "jsonrpc": "2.0",
        "method": "PlcProgram.Read",
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
