import socket

Server_host = 0.0.0.0
Server_port = 8080

#creating socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((Server_host, Server_port))
server_socket.listen(1)
print('Listening on port %s ...' % Server_port)



#binding socket



#listening socket 



#replying socket