from http.server import BaseHTTPRequestHandler, HTTPServer
from auth import authenticate
from get_perm import getpermissions
from PlcProgram_Browse import plc_program_browse
from PlcProgram_Read import plc_program_read
import json
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def format_json_response(response_text):
    try:
        parsed_response = json.loads(response_text)
        formatted_response = json.dumps(parsed_response, indent=2)
        return formatted_response
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return response_text  # Rückgabefall für den Fall eines Fehlers

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/api/browse':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            api_token = authenticate()
            var_to_browse = "\"dVisu\""
            browse_mode = "children"

            response_text_browse = plc_program_browse(api_token, var_to_browse, browse_mode)
            formatted_response_browse = format_json_response(response_text_browse)

            response_data = {
                "apiToken": api_token,
                "responseText": {
                    "browse": json.loads(formatted_response_browse),
                }
            }

            self.wfile.write(json.dumps(response_data, indent=2).encode('utf-8'))
        elif self.path.startswith('/api/read'):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Extract the variable name from the path
            var_to_read = self.path.replace('/api/read/', '')
            api_token = authenticate()

            response_text_read = plc_program_read("https://192.162.10.61/api/jsonrpc", requests.Session(), api_token, [{"name": var_to_read}])
            formatted_response_read = format_json_response(response_text_read)

            response_data = {
                "apiToken": api_token,
                "responseText": {
                    "read": json.loads(formatted_response_read)
                }
            }

            self.wfile.write(json.dumps(response_data, indent=2).encode('utf-8'))
        else:
            self.send_error(404)

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
