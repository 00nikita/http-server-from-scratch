import socket
import threading
import queue
import json
from parser import parse_request
from handlers import not_found, serve_static_file, bad_request, internal_server_error, method_not_allowed
from response import response_builder
from router import resolve
from logger import log_access, log_error


with open("config.json") as f:
    config = json.load(f)

host = config.get("host")
port = config.get("port")
workers = config.get("workers")

def handle_client(client_connection):
    #listening socket opens a client socket when a request is received
    buffer = b""
    while True:
        while b"\r\n\r\n" not in buffer:
            try:
                buffer += client_connection.recv(1024)
            except socket.timeout:
                print("Connection timed out")
                client_connection.close()
                return
        client_request = buffer# it comes in bytes, after which it is decoded and it turns to http format, which client browser sends accoriding to protocol.

        if client_request==b"":
            client_connection.close()
            return

        header_part, remaining_part = client_request.split(b"\r\n\r\n", 1)

        content_length = 0
        for line in header_part.split(b"\r\n"):
            if line.startswith(b"Content-Length:"):
                content_length = int(line.split(b":")[1].strip())
                break
        if len(remaining_part) < content_length:
            while len(remaining_part) < content_length:
                try:
                    remaining_part += client_connection.recv(1024)
                except socket.timeout:
                    print("Connection timed out")
                    client_connection.close()
                    return
        body_part = remaining_part[:content_length]
        buffer = remaining_part[content_length:]

        client_request = header_part + b"\r\n\r\n" + body_part

        #parse the incoming request
        try:
            method, path, version, query_param, headers, body = parse_request(client_request.decode())
            if path!="/login" and (not is_authenticated(headers)):
                status, response_headers, body = unauthorized(path, headers, body)
                response = response_builder(status, response_headers ,body)
                client_connection.sendall(response)
                client_ip = client_connection.getpeername()[0]
                log_error(client_ip, method, path, status, "Unauthorized access")
                client_connection.close()
                return
        except Exception as e:
            status, response_headers, body = bad_request("", {}, "")
            response = response_builder(status, response_headers ,body)
            client_connection.sendall(response)
            client_ip = client_connection.getpeername()[0]
            log_error(client_ip, "", "", status, str(e))
            client_connection.close()
            return

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
            response = response_builder(status, response_headers ,body)
            client_connection.sendall(response)
            client_ip = client_connection.getpeername()[0]
            log_error(client_ip, method, path, status, e)
            client_connection.close()
            continue

        if method == "HEAD":
            body = b""
        if method == "OPTIONS":
            body = b""
            response_headers = {"Allow": ", ".join(route.keys())}
        response = response_builder(status, response_headers ,body)
        client_connection.sendall(response)
        client_ip = client_connection.getpeername()[0]
        log_access(client_ip, method, path, status)
        if headers.get("Connection")!="keep-alive":
            client_connection.close()
            return

client_queue = queue.Queue()

def worker():
    while True:
        client_connection = client_queue.get()
        handle_client(client_connection)

#creating socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#binding socket
socket.bind((host, port))
#listen to connections 
socket.listen()

for _ in range(workers):
    thread = threading.Thread(target=worker)
    thread.start()
#acccept connection
while True:
    client_connection, client_address = socket.accept()
    client_connection.settimeout(5.0)
    client_queue.put(client_connection) #producer model


#close listening socket
socket.close()
