def home():
    with open("pages/index.html") as f:
        body = f.read()
    return "HTTP/1.1 200 OK", body
def about():
    with open("pages/about.html") as f:
        body = f.read()
    return "HTTP/1.1 200 OK", body
def login_page():
    with open("pages/login.html") as f:
        body = f.read()
    return "HTTP/1.1 200 OK", body
def process_login(headers, body):
    with open("pages/login_success.html") as f:
        body = f.read()
    return "HTTP/1.1 200 OK", body
def not_found():
    with open("pages/not_found.html") as f:
        body = f.read()
    return "HTTP/1.1 404 Not Found", body