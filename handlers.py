def home():
    with open("pages/index.html") as f:
        page = f.read()
    return "HTTP/1.1 200 OK", page
def about():
    with open("pages/about.html") as f:
        page = f.read()
    return "HTTP/1.1 200 OK", page
def login_page():
    with open("pages/login.html") as f:
        page = f.read()
    return "HTTP/1.1 200 OK", page
def process_login(headers, body):
    with open("pages/login_success.html") as f:
        page = f.read()
    username = body["username"]
    page = page.replace("{{username}}", username)
    return "HTTP/1.1 200 OK", page
def not_found():
    with open("pages/not_found.html") as f:
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
    with open(file_path) as f:
        content = f.read()
    return "HTTP/1.1 200 OK", content, content_type