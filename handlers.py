def home():
    with open("pages/index.html", "rb") as f:
        page = f.read()
    return "HTTP/1.1 200 OK", page
def about():
    with open("pages/about.html", "rb") as f:
        page = f.read()
    return "HTTP/1.1 200 OK", page
def login_page():
    with open("pages/login.html", "rb") as f:
        page = f.read()
    return "HTTP/1.1 200 OK", page
def process_login(headers, body):
    with open("pages/login_success.html", "rb") as f:
        page = f.read()
    username = body["username"]
    body = body.encode()  # Encode the body to bytes
    page = page.replace("{{username}}", username)
    body = body.decode()
    return "HTTP/1.1 200 OK", page
def not_found():
    with open("pages/not_found.html", "rb") as f:
        page = f.read()
    return "HTTP/1.1 404 Not Found", page
def serve_static_file(path):
    file_path = path.split("/", 1)[1]
    if file_path.endswith(".css"):
        content_type = "text/css"
    elif file_path.endswith(".js"):
        content_type = "application/javascript"
    elif file_path.endswith(".png"):
        content_type = "image/png"
    else:
        content_type = "application/octet-stream"
    with open(file_path, "rb") as f:
        content = f.read()
    return "HTTP/1.1 200 OK", content, content_type