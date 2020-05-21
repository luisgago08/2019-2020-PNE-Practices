import socket
#import termcolor

IP = '127.0.0.1' #212.128.253.149
PORT = 8080

# --- step 1: creating the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# --- step 2: Bind the socket to the server's IP and PORT
ls.bind((IP, PORT))

# --- step 3: convert into a listening socket
ls.listen()

print('Server is configured!')

while True:

    try:
        # --- step 4: wait for client to connect
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print(f"Server is done!")
        ls.close()
        exit()
    else:
        # --- step 5: receiving information from the client
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()

        print(f"Received message: ", end="")
        #termcolor.cprint(msg, "green")

        # --- step 6: send a response message to the client
        response = f"ECHO: {msg}\n"
        cs.send(response.encode())

        cs.close()
