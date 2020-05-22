import http.server
import socketserver
from pathlib import Path

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        print(self.requestline)

        # Analize the request line
        req_line = self.requestline.split(' ')

        # Get the path. It always start with the / symbol
        path = req_line[1]

        # separamos el path,  lo que está antes del ? y lo que está depues
        arguments = path.split("?")

        action_echo = arguments[0]

        if action_echo == "/":  # Manda la pg principal
            contents = Path("form-EX02.html").read_text()
            status = 200

        elif action_echo == "/myserver":  # Escribe en la pg principal
            input = arguments[1]
            # Separar el mensaje de lo que escribe el cliente, ahora puede haber dos iguales si activas lo de las mayúsculas
            input_name = input.split("=")[-1]
            input_value = input.split("=")[1]
            input_value_check_off = input_value.split("&")[0]
            #input_value_check_on = input_value.split("&")[1]

            if "on" in input_name:
                contents = Path("form-EX01.html").read_text()
                # Para añadir el mensaje del cliente
                contents = contents + f"<p>{input_value_check_off.upper()}</p>"
                contents = contents + f'<a href="/">Main page</a>'
                status = 200

            else:
                contents = Path("form-EX01.html").read_text()
                # Para añadir el mensaje del cliente
                contents = contents + f"<p>{input_value}</p>"
                contents = contents + f'<a href="/">Main page</a>'
                status = 200
        else:
            # -- Resource NOT FOUND
            print("ERROR: Not found")

            # Message to send back to the clinet
            contents = Path("Error.html").read_text()

            # Status code is NOT FOUND
            status = 404



        # Generating the response message
        self.send_response(status)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()