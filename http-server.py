import socket
import parser_request from parser

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
    client_request = client_connection.recv(1024).decode() # it comes in bytes, after which it is decoded and it turns to http format, which client browser sends accoriding to protocol.
    request_line = client_request.splitlines()[0]
    method, path, version = request_line.split()
    method, path, version, query_param, headers =parser_request(client_request)
    print("method:", method)    
    print("path:", path)
    print("version:", version)
    print("query param:", query_param)
    print("Headers:", headers)
    if path == "/":
        body = "Home Page"
        status = "HTTP/1.1 200 OK"
    elif path == "/about":
        body = "About Page"
        status = "HTTP/1.1 200 OK"
    else:
        body = "404: PAGE NOT FOUND"
        status = "HTTP/1.1 404 NOT FOUND"

    response = f"{status}\r\nContent-Length: {len(body)}\r\n\r\n{body}"
    client_connection.sendall(response.encode())
    # client_connection.close()

#close listening socket
socket.close()