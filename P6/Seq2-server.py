import http.server
import socketserver
from pathlib import Path
from Seq1 import Seq

FOLDER = "../Session-04/"
TEXT = ".txt"

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

        action = arguments[0]
        sequences = ["ACCTTGAA", "TGCATGCA", "GGGCATTA", "CTCTCAGA", "AGTAATGC"]

        if path == "/":  # Manda la pg principal
            # contents = Path("form-1.html").read_text()
            # contents = Path("form-2.html").read_text()
            # contents = Path("form-3.html").read_text()
            contents = Path("form-4.html").read_text()

            status = 200

        elif action == "/ping":  # Escribe en la pg principal
            # después del ?
            contents = """
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                          <title> PING </title >
                        </head >
                        <body>
                        <h2> PING OK!</h2>
                        <p> The SEQ2 server in running... </p>
                        <a href="/">Main page</a>
                        </body>
                        </html>
                        """
            status = 200
        elif action == "/get":
            # Coger lo que está despues del interrogante (n=2)
            number = arguments[1]
            # Coger el número que seleccionas
            n = int(number.split("=")[1])
            seq = sequences[n]
            # POnemos la f antes para que así te añada las seq y el número seleccionado
            contents = f""" 
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                          <title> Get </title >
                        </head >
                        <body>
                        <h2> Sequence number {n}</h2>
                        <p>{seq} </p>
                        <a href="/">Main page</a>
                        </body>
                        </html>
                        """
            status = 200

        elif action == "/gene":
            gene_and_name = arguments[1]
            name = gene_and_name.split("=")[1]
            s = Seq("")
            s_str = str(s.read_fasta(FOLDER + name + TEXT))

            contents = f"""
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                          <title> GENE </title >
                        </head >
                        <body>
                        <h2> Gene: {name}</h2>
                        <textarea readonly rows="20" cols="80"> {s_str} </textarea>
                        <br>
                        <br>
                        <a href="/">Main page</a>
                        </body>
                        </html>
                        """
            status = 200
        elif action == "/operation":
            msg_op = arguments[1]
            # Cogemos msg = y el mensaje
            msg = msg_op.split("&")[0]
            # Ahora cogemos solo la cadena que se introduce
            gene = msg.split("=")[1]

            # Creamos la secuencia
            seq = Seq(gene)

            # la operación
            name_op = msg_op.split("&")[1]
            # Operación seleccionada
            operation_select = name_op.split("=")[1]
            if operation_select == "Info":
                seq_length = seq.len()
                number_of_A = seq.count_base("A")
                porcentaje_A = "{:.1f}".format(100 * number_of_A / seq_length)
                number_of_G = seq.count_base("G")
                porcentaje_G = "{:.1f}".format(100 * number_of_G / seq_length)
                number_of_T = seq.count_base("T")
                porcentaje_T = "{:.1f}".format(100 * number_of_T / seq_length)
                number_of_C = seq.count_base("C")
                porcentaje_C = "{:.1f}".format(100 * number_of_C / seq_length)

                contents_of_operations = f"""
                <p>Total length: {seq_length}</p>
                <p>A: {number_of_A} ({porcentaje_A}%)</p>
                <p>C: {number_of_C} ({porcentaje_C}%)</p>
                <p>G: {number_of_G} ({porcentaje_G}%)</p>
                <p>T: {number_of_T} ({porcentaje_T}%)</p>"""

            elif operation_select == "Comp":
                contents_of_operations = seq.complement()

            # Para cuendo sea operation_select == "Rev":
            else:
                contents_of_operations = seq.reverse()

            contents = f"""
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                          <title> OPERATION </title >
                        </head >
                        <body>
                        <h2> Sequence </h2>
                        <p>{seq}</p>
                        <h2> Operation: </h2>
                        <p>{operation_select}</p>
                        <h2> Result: </h2>
                        <p>{contents_of_operations}</p>
                        <br>
                        <br>
                        <a href="/">Main page</a>
                        </body>
                        </html>
                        """
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