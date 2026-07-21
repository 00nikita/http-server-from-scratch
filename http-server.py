import socket

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
    print("method:", method)    
    print("path:", path)
    print("version:", version)
    lines = client_request.splitlines()
    headers = {}
    for line in lines[1:]:
        if line=="":
            break
        key, value = line.split(":", 1)
        headers[key]=value.strip()
    print("Headers:", headers) 
    response = 'HTTP/1.0 200 OK\n\nHello World\n'
    client_connection.sendall(response.encode())
    # client_connection.close()

#close listening socket
socket.close()