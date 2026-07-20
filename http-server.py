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
client_connection = None
while True:
    if(client_connection==None):
        client_connection, client_address = socket.accept()
    #listening socket opens a client socket when a request is received
    client_request = client_connection.recv(1024).decode() # it comes in bytes, after which it is decoded and it turns to http format, which client browser sends accoriding to protocol.
    print(client_request)
    response = 'HTTP/1.0 200 OK\n\nHello World\n'
    client_connection.sendall(response.encode())
    # client_connection.close()

#close listening socket
socket.close()