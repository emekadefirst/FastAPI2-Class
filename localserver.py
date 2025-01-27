import socke172.31.0.1t
# from http.server import BaseHTTPRequestHandler, HTTPServer


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 8000))

while True:
    server_socket.listen(1)

    client_socket, client_address = server_socket.accept()
    print(f"Connetion from {client_address}")

    # send and recieve data
    data = client_socket.recv(1024).decode()
    print(f"Client says: {data}")

    client_socket.send("Hello, server!".encode())
