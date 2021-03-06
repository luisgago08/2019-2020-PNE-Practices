import socket
import termcolor

IP = '212.128.253.149'
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

count_connect = 0
list_ip_port = []

while count_connect < 5:

    try:
        # --- step 4: wait for client to connect
        (cs, client_ip_port) = ls.accept()
        list_ip_port.append(client_ip_port)

    except KeyboardInterrupt:
        print(f"Server is done!")
        ls.close()
        exit()
    else:
        # --- step 5: receiving information from the client
        count_connect = count_connect + 1
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()

        print(f"CONNECTION {count_connect}.Client IP, PORT: ({IP}, {PORT})")
        print(f"Received message: ")
        termcolor.cprint(msg, "green")
        print(f"Waiting for clients to connect")

        # --- step 6: send a response message to the client
        response = f"ECHO: {msg}\n"
        cs.send(response.encode())

        cs.close()

print("The following clients have connected to the server")
for e in range(len(list_ip_port)):
    print(f"Client {e}: {list_ip_port[e]}")
