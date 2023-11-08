from auth import authenticate
from get_perm import getpermissions

if __name__ == "__main__":
    # Zuerst authentifizieren und den API-Token erhalten
    api_token = authenticate()
    print(f"API-Token: {api_token}")

    # Dann die getpermissions-Funktion mit dem API-Token aufrufen
    response_text = getpermissions(api_token)
    print(response_text)
