import http.server
import socketserver
from pathlib import Path

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# -- FUNCTIONS
def msg(pathmessage):
    list1 = pathmessage.partition("echo?=msg")
    message = list1[2]
    return message


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        print(self.requestline)
        print(self.path)

        # Open the form1.html file
        # Read the index from the file

        if self.path == "/":
            contents = Path('form-EX01.html').read_text()
        elif "/echo" in self.path:
            a = self.path.partition("/echo?msg=")
            mensaje = a[2]
            mensaje1 = mensaje.replace("+", " ")
            contents = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset= "utf-8">
                    <title> RESPONSE </title>
                <head> 
                <body>
                    <h1> Received Message </h1>
                    <p> {mensaje1} </p>
                <a href="http://127.0.0.1:8080/">Main page</a>
                </body>
                </html>
                """
        else:
            contents = Path('Error.html').read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

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