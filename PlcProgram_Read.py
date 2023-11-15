import requests
import json
from requests.exceptions import ConnectTimeout

MAX_RETRIES = 3

def plc_program_read(url: str, session: requests.Session, token: str, variables):
    requests_list = []

    for i, var in enumerate(variables, start=1):
        requests_list.append({
            "id": i,
            "jsonrpc": "2.0",
            "method": "PlcProgram.Read",
            "params": {
                "var": f"\"dVisu\".{var['name']}"
            }
        })

    payload = json.dumps(requests_list)
    
    # Define headers here
    headers = {
        'Content-Type': 'application/json',
        'Content-Length': str(len(payload)),
        'Host': '192.162.10.61',
        'User-Agent': 'PostmanRuntime/7.33.0',
        'X-Auth-Token': token
    }

    try:
        response = session.post(url, headers=headers, data=payload, verify=False)
        response_json = response.json()

        results = {}
        for var, res in zip(variables, response_json):
            results[var['name']] = res['result']

        return results
    except requests.exceptions.ConnectTimeout as e:
        print(f"Connection timeout: {e}")
        # Handle the timeout exception, e.g., retry or raise an error
        raise