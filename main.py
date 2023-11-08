from auth import authenticate
from get_perm import getpermissions

if __name__ == "__main__":
    """
    Hauptprogramm zur Authentifizierung und Berechtigungsabfrage über die API.

    1. Authentifiziert den Benutzer und erhält einen API-Token.
    2. Ruft die getpermissions-Funktion auf, um die Benutzerberechtigungen abzurufen.

    Args:
        None

    Returns:
        None
    """

    # Zuerst authentifizieren und den API-Token erhalten
    api_token = authenticate()
    print(f"API-Token: {api_token}")

    # Dann die getpermissions-Funktion mit dem API-Token aufrufen
    response_text = getpermissions(api_token)
    print(response_text)
