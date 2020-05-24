import http.server
import http.client
import socketserver
from pathlib import Path
import json

# -- THE PORT
PORT = 8080
Server = "rest.ensembl.org"
Parameters = "?content-type=application/json"

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

        # separamos el path,  lo que está antes del ? y lo que está depues
        arguments = path.split("?")

        endpoint = arguments[0]

        if endpoint == "/":  # Main page
            contents = Path("index.html").read_text()
            status = 200

        elif endpoint == "/listSpecies":
            # Get what is after ? (limit=10)
            limit_number = arguments[1]
            # Get selected specie
            limit = limit_number.split("=")[1]
            Endpoint = "/info/species"
            # This is the req line to search the info
            Request_line = Endpoint + Parameters

            # Create a variable with the data, form the JSON received
            name_specie = server(Request_line)["species"]

            count_species = 0
            for element in name_specie:
                count_species = count_species + 1
            contents = f""" 
                                <!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8" >
                                  <title> List of species </title >
                                </head >
                                <body style="background-color: lightblue;">
                                <p> The total number of species in the ensembl is: {count_species} </p>
                                </body>
                                </html>
                                """
            if limit == "":
                contents += f"""<a href="/">Main page</a>"""
                status = 200

            elif int(limit) > count_species:
                contents = Path('Error.html').read_text()
                status = 404
            else:
                contents = contents + f""" <p> The limit you have selected is: {limit}</p>
                                <p> The name of the species are: </p>"""

                status = 200
                for element in name_specie[:int(limit)]:  # Fron the beginning to the limit introduced by the client
                    contents += f""" <p>   • {element["common_name"]}</p>"""
                contents += f"""<a href="/">Main page</a>"""

