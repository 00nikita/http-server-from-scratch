from datetime import datetime, timezone

def response_headers_builder(page, headers):
    now = datetime.now(timezone.utc)
    date = now.strftime("%a, %d %b %Y %H:%M:%S GMT")
    response_headers = {
        "Content-Length": str(len(page)),
        "Server": "NikhithaHTTP/1.0",
        "Date": date,
        "Connection": "close"
    }
    response_headers.update(headers)
    return response_headers

def home(path, headers, body):
    with open("pages/index.html", "rb") as f:
        page = f.read()
    response_headers = response_headers_builder(page, {"Content-Type": "text/html"})
    return "HTTP/1.1 200 OK", response_headers, page

def about(path, headers, body):
    with open("pages/about.html", "rb") as f:
        page = f.read()
    response_headers = response_headers_builder(page, {"Content-Type": "text/html"})
    return "HTTP/1.1 200 OK", response_headers, page

def login_page(path, headers, body):
    with open("pages/login.html", "rb") as f:
        page = f.read()
    response_headers = response_headers_builder(page, {"Content-Type": "text/html"})
    return "HTTP/1.1 200 OK", response_headers, page

def welcome(path, headers, body):
    with open("pages/welcome.html", "rb") as f:
        page = f.read()
    response_headers = response_headers_builder(page, {"Content-Type": "text/html"})
    return "HTTP/1.1 200 OK", response_headers, page

def process_login(path, headers, body):
    response_headers = response_headers_builder(b"", {"Location": "/welcome"})
    return "HTTP/1.1 302 Found", response_headers, b""

def not_found(path, headers, body):
    with open("pages/not_found.html", "rb") as f:
        page = f.read()
    response_headers = response_headers_builder(page, {"Content-Type": "text/html"})
    return "HTTP/1.1 404 Not Found", response_headers, page

def bad_request(path, headers, body):
    with open("pages/bad_request.html", "rb") as f:
        page = f.read()
    response_headers = response_headers_builder(page, {"Content-Type": "text/html"})
    return "HTTP/1.1 400 Bad Request", response_headers, page

def serve_static_file(path, headers, body):
    file_path = path.split("/", 1)[1]
    if file_path.endswith(".css"):
        content_type = "text/css"
    elif file_path.endswith(".js"):
        content_type = "application/javascript"
    elif file_path.endswith(".png"):
        content_type = "image/png"
    else:
        content_type = "application/octet-stream"
    try:
        with open(file_path, "rb") as f:
            page = f.read()
    except FileNotFoundError:
        return not_found(path, headers, body)

    response_headers = response_headers_builder(page, {"Content-Type": content_type})
    return "HTTP/1.1 200 OK", response_headers, page