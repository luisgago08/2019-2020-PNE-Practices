import http.server
import http.client
import socketserver
from pathlib import Path
import json

# -- THE PORT
PORT = 8080
Server = "rest.ensembl.org"
Params = "?content-type=application/json"

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


def server(Request_line):
    # Connect with the server
    conn = http.client.HTTPConnection(Server)
    try:
        conn.request("GET", Request_line)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # Read the response message from the server
    r1 = conn.getresponse()

    # Read the response's body
    data = r1.read().decode("utf-8")
    data1 = json.loads(data)

    return data1
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

        # Separamos el path antes del ? y depués
        arguments = path.split("?")

        endpoint = arguments[0]

        if endpoint == "/":  # Main page
            contents = Path("index.html").read_text()
            status = 200
        # Option1
        elif endpoint == "/listSpecies":
            try:
                # Get what is after ? (limit=10)
                limit_numb = arguments[1]
                # Get selected specie
                limit = limit_numb.split("=")[1]
                Endpoint = "/info/species"
                # This is the req line to search the info
                Request_line = Endpoint + Params

                # Create a variable with the data, form the JSON received
                name_specie = server(Request_line)["species"]

                count = 0
                for element in name_specie:
                    count = count + 1
                contents = f""" 
                                    <!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                    <meta charset = "utf-8" >
                                      <title> List of species </title >
                                    </head >
                                    <body style="background-color: lightblue;">
                                    <p> The total number of species in the ensembl is: {count} </p>
                                    </body>
                                    </html>
                                    """
                if limit == "":
                    contents += f"""<a href="/">Main page</a>"""
                    status = 200

                elif int(limit) > count:
                    contents = Path('Error.html').read_text()
                    status = 404
                else:
                    contents += f""" <p> The limit you have selected is: {limit}</p>
                                    <p> The name of the species are: </p>"""

                    status = 200
                    for element in name_specie[:int(limit)]:  # From beginning to limit
                        contents += f""" <p> - {element["common_name"]}</p>"""
                    contents += f"""<a href="/">Main page</a>"""
            except ValueError:
                contents = Path('Error.html').read_text()
                status = 404

        # Option2
        elif endpoint == "/infoKaryotype":
            # Get what is after ? (specie=mouse)
            specie_name = arguments[1]
            # Get selected specie
            name_specie = specie_name.split("=")[1]
            Endpoint = "/info/assembly/"
            # This is the req line to search the info
            Request_line = Endpoint + name_specie + Params
            try:
                # Check if the req line is ok
                Request_line.isidentifier()
                # Create a variable with the data
                kar_sp = server(Request_line)
                contents = f""" 
                                   <!DOCTYPE html>
                                   <html lang = "en">
                                   <head>
                                   <meta charset = "utf-8" >
                                     <title> Karyotype of a specific specie </title >
                                   </head >
                                   <body>
                                   <body style="background-color: lightblue;">
                                   <p>The names of the chromosomes are:</p>
                                   </body>
                                   </html> 
                                   """
                status = 200
                for element in kar_sp["karyotype"]:
                    contents += f"""<p>{element}</p>"""
                contents += f"""<a href="/">Main page</a>"""

            except KeyError:
                contents = Path("Error.html").read_text()
                status = 404

        # Option3
        elif endpoint == "/ChromLength":
            # Get what is after ? (specie=mouse&chromo=18)
            sp_chromo = arguments[1]
            # Get the specie that we select
            name_specie = sp_chromo.split("&")[0].split("=")[1]
            numb_chromo = sp_chromo.split("&")[1].split("=")[1]
            Endpoint = "/info/assembly/"
            # This is the req line to search the info
            Request_line = Endpoint + name_specie + "/" + numb_chromo + Params
            try:
                # Check if the req line is ok
                Request_line.isidentifier()
                # Create a variable with the data
                l_chromosome = server(Request_line)
                contents = f""" 
                                    <!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                    <meta charset = "utf-8" >
                                        <title> Length of the selected chromosome </title >
                                    </head >
                                    <body>
                                    <body style="background-color: lightblue;">
                                    <p> The length of the chromosome is: {l_chromosome["length"]}</p>
                                    <a href="/">Main page</a>
                                    </body>
                                    </html>
                                    """
                status = 200

            except KeyError:
                contents = Path("Error.html").read_text()
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
        print("Stopped by the user")
        httpd.server_close()
