import socket
from parser import parse_request
from handlers import home, about, login_page, process_login, not_found, serve_static_file, welcome
from response import response_builder
from router import routes

host = "0.0.0.0"
port = 8000

#creating socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#binding socket
socket.bind((host, port))
#listen to connections 
socket.listen()
#acccept connection
while True:
    client_connection, client_address = socket.accept()
    #listening socket opens a client socket when a request is received
    client_request = client_connection.recv(1024).decode()# it comes in bytes, after which it is decoded and it turns to http format, which client browser sends accoriding to protocol.
    print(client_request)
    #parse the incoming request
    method, path, version, query_param, headers, body = parse_request(client_request)
    print("method:", method)
    print("path:", path)
    print("version:", version)
    print("query param:", query_param)
    print("Headers:", headers)
    print("Body:", body)

    #route the requests to the appropriate handler
    handler = routes.get((method, path))
    if handler:
        status, response_headers, body = handler(path, headers, body)
    elif method == "GET" and path.startswith("/static/"):
        status, response_headers, body = serve_static_file(path, headers, body)
    else:
        status, response_headers, body = not_found(path, headers, body)
    response = response_builder(status, response_headers ,body)
    client_connection.sendall(response)
    # client_connection.close()

#close listening socket
socket.close()
