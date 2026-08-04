import socket
from parser import parse_request
from handlers import not_found, serve_static_file, bad_request, internal_server_error, method_not_allowed
from response import response_builder
from router import resolve

host = "0.0.0.0"
port = 8000

#creating socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#binding socket
socket.bind((host, port))
#listen to connections 
socket.listen()
#acccept connection
keep_alive = False
while True:
    if not keep_alive:
        client_connection, client_address = socket.accept()
        buffer = b""
    #listening socket opens a client socket when a request is received
    while b"\r\n\r\n" not in buffer:
        buffer +=client_connection.recv(1024)
    client_request = buffer.decode()# it comes in bytes, after which it is decoded and it turns to http format, which client browser sends accoriding to protocol.
    
    header_part, remaining_part = client_request.split("\r\n\r\n", 1)

    content_length = 0
    for line in header_part.split("\r\n"):
        if line.startswith("Content-Length:"):
            content_length = int(line.split(":")[1].strip())
            break
    if len(remaining_part.encode()) < content_length:
        while len(remaining_part.encode()) < content_length:
            buffer += client_connection.recv(1024)

            client_request = buffer.decode()
            header_part, remaining_part = client_request.split("\r\n\r\n", 1)
    else:
        body_part = remaining_part.encode()[:content_length]
        remaining_part = remaining_part.encode()[content_length:]

    #parse the incoming request
    try:
        method, path, version, query_param, headers, body = parse_request(client_request)
    except Exception as e:
        status, response_headers, body = bad_request("", {}, "")
        response = response_builder(status, response_headers ,body)
        client_connection.sendall(response)
        client_connection.close()
        continue

    print("method:", method)
    print("path:", path)
    print("version:", version)
    print("query param:", query_param)
    print("Headers:", headers)
    print("Body:", body)

    #route the requests to the appropriate handler
    try:
        handler, route = resolve(method, path)
        if method == "OPTIONS":
           if route:
              status = "HTTP/1.1 200 OK"
              response_headers = {
                  "Allow": ", ".join(route.keys())
              }
              body = b""
           else:
               status, response_headers, body = not_found(path, headers, body)

        elif handler:
            status, response_headers, body = handler(path, headers, body)
        elif route:
            allowed_methods = ", ".join(route.keys())
            status, response_headers, body = method_not_allowed(
            path,
            headers,
            body,
            allowed_methods
        )
        else:
            status, response_headers, body = not_found(path, headers, body)
    except Exception as e:
        print("Internal Server Error:", e)
        status, response_headers, body = internal_server_error(path, headers, body)
    if method == "HEAD":
        body = b""
    if method == "OPTIONS":
        body = b""
        response_headers = {"Allow": ", ".join(route.keys())}
    response = response_builder(status, response_headers ,body)
    client_connection.sendall(response)
    if headers.get("Connection")=="keep-alive":
        keep_alive = True
    else:
        keep_alive = False
        client_connection.close()

#close listening socket
socket.close()
